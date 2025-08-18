import numpy as np
from equations import T_ring_phi, T_ring, resonance_waves
import matplotlib.pyplot as plt
import streamlit as st


st.title("Ring Resonator Transmission Demo")

st.sidebar.header("Input Parameters")

st.write("Transmission Equation:")
st.write(r"$T = \frac{(\sigma + a)^2 - 4\sigma a \cos^2(\frac{kL}{2})}{(\sigma a + 1)^2 - 4\sigma a \cos^2(\frac{kL}{2})}$")
st.write("Resonance Equation:")
st.write(r"$kL = 2\pi n$")

c = 3e8 # speed of light in m/s

# Input parameters for T_ring
st.sidebar.subheader("T_ring Parameters")
sigma = st.sidebar.slider("sigma", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
a = st.sidebar.slider("a", min_value=0.0, max_value=1.0, value=0.8, step=0.01)
L = st.sidebar.slider("L (um)", min_value=0.1, max_value=100.0, value=50.0, step=1.0)

# Wavelength or k
wavelength_min = st.sidebar.number_input("Wavelength min (μm)", min_value=0.1, max_value=10.0, value=1.4, step=0.01)
wavelength_max = st.sidebar.number_input("Wavelength max (μm)", min_value=0.1, max_value=10.0, value=1.7, step=0.01)
num_points = st.sidebar.number_input("Number of points", min_value=10, max_value=10000, value=1000, step=10)
omega_min = st.sidebar.number_input("Omega min (Hz)", min_value=0.1, max_value=10.0, value=1.4, step=0.01)
omega_max = st.sidebar.number_input("Omega max (Hz)", min_value=0.1, max_value=10.0, value=1.7, step=0.01)
T_max = st.sidebar.number_input("T max", min_value=0.0, max_value=1.0, value=1.0, step=0.01)
T_min = st.sidebar.number_input("T min", min_value=0.0, max_value=1.0, value=0.0, step=0.01)

wavelengths = np.linspace(wavelength_min, wavelength_max, int(num_points))
# omega = np.linspace(omega_min, omega_max, int(num_points))
# wavelengths = 2 * np.pi * c / omega

k = 2 * np.pi / wavelengths
T = T_ring(sigma, a, k, L)

resonance_dict = resonance_waves(wavelength_min, wavelength_max, L)
resonance_waves = list(resonance_dict.values())
resonance_n = list(resonance_dict.keys())
resonance_list_str = ", ".join([f'{wave:.4f}' for wave in resonance_waves])
st.write(f"Resonance Wavelength List (um): {resonance_list_str}")

include_resonance = st.checkbox("Include Resonance", value=True)

fig, ax = plt.subplots()
ax.plot(wavelengths, T, label="Transmission", linestyle='-')
if include_resonance:
    ax.vlines(resonance_waves, T_min, T_max, color='red', linestyle='--')
# ax.plot(omega, T, label="Transmission", linestyle='-', marker='.')
ax.set_xlabel("Wavelength (μm)")
# ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Transmission")
ax.set_title("Ring Resonator Transmission Spectrum")
ax.set_ylim(T_min, T_max)
ax.grid(True)
ax.legend()

st.pyplot(fig)

st.markdown("""
This demo shows the transmission spectrum of a ring resonator as a function of wavelength.
Adjust the parameters in the sidebar to see how the transmission changes.
""")
