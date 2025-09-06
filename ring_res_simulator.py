import streamlit as st
import meep as mp
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Video
import shutil
import os
import glob
from PIL import Image

st.title("Meep Simulation of Ring Resonator")


with st.sidebar:
    st.header("Input Parameters")

    st.subheader("Geometry Parameters")
    r = st.number_input("Radius (um)", min_value=0.1, max_value=100.0, value=10.0, step=0.1)
    wg_width = st.number_input("Waveguide Width (um)", min_value=0.1, max_value=10.0, value=0.5, step=0.1)
    gap = st.number_input("Gap (um)", min_value=0.1, max_value=10.0, value=0.3, step=0.1)
    wvl = st.number_input("Wavelength (um)", min_value=0.1, max_value=10.0, value=1.55, step=0.01)
    resolution = st.number_input("Resolution", value = 20, step = 1)

# Create a ring resonator with a radius of 10um

# Define materials
Si = mp.Medium(index=3.45)
SiO2 = mp.Medium(index=1.45)

# Define geometrical parameters
d_pml = 1 # thickness of the pml
d_pad = 1 # thickness of padding around geometry
r_in = r - wg_width / 2
r_out = r + wg_width / 2
wg_length = 2 * r_out + 2 * d_pad + 2 * d_pml # length of the waveguide

pml = [mp.PML(d_pml)]
Sx = 2 * r_out + 2 * d_pad + 2 * d_pml # width of the cell
Sy = 2 * r_out + 4 * d_pad + 2 * d_pml # length of the cell
st.sidebar.write(f"Sx (cell width) = {Sx}")
st.sidebar.write(f"Sy (cell length) = {Sy}")
st.sidebar.write(f"waveguide length = {wg_length}")

geometry = [mp.Cylinder(radius=r_out, material=Si, center=mp.Vector3(0,d_pad*1.5)),
            mp.Cylinder(radius=r_in, material=SiO2, center=mp.Vector3(0,d_pad*1.5)),
            mp.Block(size=(wg_length,wg_width), center=mp.Vector3(0, -r_out+d_pad*1.5-gap), material=Si)]

# Create Eigenmode pulse source
fcen = 0.15
width = 0.1
fwidth = width * fcen
src=mp.GaussianSource(frequency=fcen, fwidth=fwidth)
source = [mp.EigenModeSource(src=src, eig_band=1,
        eig_kpoint = (1,0),
        size=mp.Vector3(0,1),
        center=mp.Vector3(-0.4*Sx, -r_out+d_pad*1.5-gap))
        ]

# Set up simulation
sim = mp.Simulation(
    resolution=20,
    default_material=SiO2,
    cell_size=mp.Vector3(Sx,Sy),
    geometry=geometry,
    boundary_layers=pml,
    sources=source
)

fig, ax = plt.subplots()
sim.plot2D(ax=ax)
ax.set_title("Ring Resonator")
ax.set_xlabel("x (um)")
ax.set_ylabel("y (um)")
ax.set_aspect("equal")
ax.grid(True, linestyle='--', alpha=0.5)

with st.expander("Plot 2D Geometry of Simulation", expanded=True):
    st.pyplot(fig)


with st.expander("Simulation Parameters", expanded=True):
    sim_step = st.number_input("At every N", value = 2.0, step = 0.1)
    st.caption("Calls the function at every N time units")
    until = st.number_input("Until", value = 600, step = 10)
    st.caption("Number of time units to run the simulation")

if st.button("Run Simulation"):
    if os.path.exists("png_outputs"):
        shutil.rmtree("png_outputs")
    sim.use_output_directory("png_outputs")
    sim.run(mp.at_beginning(mp.output_epsilon),
            mp.at_every(sim_step, 
                        mp.output_png(mp.Ez, "-Zc dkbluered"), 
                        mp.output_png(mp.Ey, "-Zc dkbluered")),
            until=until)
    st.success("Simulation completed successfully")


if st.button("Generate Ez GIF"):

    frames = []
    imgs = glob.glob("png_outputs/app-ez*")
    imgs.sort()
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    print(f"Number of frames: {len(frames)}")

    frames[0].save('simulation_ez.gif', format='GIF', append_images=frames[1:], save_all=True, loop=0)

    st.success("Ez GIF generated successfully")

if st.button("Generate Ey GIF"):
    frames = []
    imgs = glob.glob("png_outputs/app-ey*")
    imgs.sort()
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    print(f"Number of frames: {len(frames)}")

    frames[0].save('simulation_ey.gif', format='GIF', append_images=frames[1:], save_all=True, loop=0)

    st.success("Ey GIF generated successfully")


if os.path.exists('simulation_ez.gif'):
    with st.expander("Simulation Ez GIF", expanded=True): 
        st.image(f"simulation_ez.gif")

if os.path.exists('simulation_ey.gif'):
    with st.expander("Simulation Ey GIF", expanded=True): 
        st.image(f"simulation_ey.gif")


