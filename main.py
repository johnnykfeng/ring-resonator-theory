import numpy as np
from equations import *
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
L = st.sidebar.slider("L (um)", min_value=0.1, max_value=3000.0, value=300.0, step=10.0)

# Wavelength or k
wavelength_min = st.sidebar.number_input("Wavelength min (μm)", 
min_value=0.1, max_value=10.0, value=1.54, step=0.001)
wavelength_max = st.sidebar.number_input("Wavelength max (μm)", 
min_value=0.1, max_value=10.0, value=1.56, step=0.001)
num_points = st.sidebar.number_input("Number of points", min_value=10, max_value=10000, value=5000, step=10)
omega_min = st.sidebar.number_input("Omega min (Hz)", min_value=0.1, max_value=10.0, value=1.4, step=0.01)
omega_max = st.sidebar.number_input("Omega max (Hz)", min_value=0.1, max_value=10.0, value=1.7, step=0.01)
T_max_plot = st.sidebar.number_input("T max", min_value=0.0, max_value=1.0, value=1.0, step=0.01)
T_min_plot = st.sidebar.number_input("T min", min_value=0.0, max_value=1.0, value=0.0, step=0.01)

wavelengths = np.linspace(wavelength_min, wavelength_max, int(num_points))
# omega = np.linspace(omega_min, omega_max, int(num_points))
# wavelengths = 2 * np.pi * c / omega

k = 2 * np.pi / wavelengths
T = T_ring(sigma, a, k, L)

resonance_waves = resonance_waves(wavelength_min, wavelength_max, L)
resonance_waves_values = list(resonance_waves.values())
with st.expander("Resonance Wavelength List (um)"):
    st.write(resonance_waves)

include_resonance = st.checkbox("Include Resonance", value=True)

fig, ax = plt.subplots()
ax.plot(wavelengths, T, label="Transmission", linestyle='-')
if include_resonance:
    ax.vlines(resonance_waves_values, T_min_plot, T_max_plot, color='red', linestyle='--', label="Resonance")
# ax.plot(omega, T, label="Transmission", linestyle='-', marker='.')
ax.set_xlabel("Wavelength (μm)")
# ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Transmission")
ax.set_title("Ring Resonator Transmission Spectrum")
ax.set_ylim(T_min_plot, T_max_plot)
ax.grid(True)
ax.legend(loc='lower right')

st.pyplot(fig)

st.write(f"T_max: {T_max(a, sigma):.3f}")
st.write(f"T_min: {T_min(a, sigma):.3f}")
st.write(f"Extinction Ratio: {extinction_ratio(a, sigma):.3f}")
st.write(f"Linewidth: {linewidth(a, sigma):.3f}")
st.write(f"del_k_FSR: {del_k_FSR(L):.3f}")
st.write(f"del_f_FSR: {del_f_FSR(L):.3f}")

# select f_resonance from resonance_waves_values
wave_resonance = st.selectbox("Select Resonance Wavelength (um)", resonance_waves_values)
f_resonance = frequency_from_wavelength(wave_resonance)
st.write(f"f_resonance: {f_resonance*1e-6:.3f} MHz")
# f_FSR = st.selectbox("f_FSR (Hz)", resonance_waves_values)

st.write(f"Q_load: {Q_load(f_resonance, del_f_FSR(L), a, sigma):.3f}")
st.write(f"Q_ext: {Q_ext(f_resonance, del_f_FSR(L), sigma):.3f}")
st.write(f"Q_ring: {Q_ring(f_resonance, del_f_FSR(L), a, sigma):.3f}")
st.write(f"Escape Ratio: {escape_ratio(a, sigma, f_resonance, del_f_FSR(L)):.3f}")

