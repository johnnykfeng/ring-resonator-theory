import numpy as np

c = 3e8 # speed of light in m/s

def T_ring_phi(sigma, a, phi_0, phi_a, phi_sigma):
    numerator = (sigma + a)**2 - 4*sigma*a*np.cos((phi_0+phi_a-phi_sigma)/2)**2
    denominator = (1+sigma*a)**2 - 4*sigma*a*np.cos((phi_0+phi_a+phi_sigma)/2)**2
    return numerator/denominator

def T_ring(sigma, a, k, L):
    numerator = (sigma + a)**2 - 4*sigma*a*np.cos((k*L)/2)**2
    denominator = (1+sigma*a)**2 - 4*sigma*a*np.cos((k*L)/2)**2
    return numerator/denominator

def resonance_waves(wave_min, wave_max, L):
    n_min = np.floor(L/wave_max)
    n_max = np.floor(L/wave_min)
    n_list = np.arange(n_min+1, n_max+1)
    wave_dict = {n: L/n for n in n_list}
    return wave_dict

def linewidth(a, sigma):
    return (2/np.pi)*np.arcsin((1-a*sigma)/(np.sqrt(2*(1+a**2*sigma**2))))

def wavenumber_from_wavelength(wavelength):
    return 2*np.pi/wavelength

def wavelength_from_wavenumber(k):
    return 2*np.pi/k

def wavelength_from_frequency(frequency):
    return c/frequency

def frequency_from_wavelength(wavelength):
    return c/wavelength

def frequency_from_wavenumber(k):
    return c*k/2/np.pi

def wavenumber_from_frequency(frequency):
    return 2*np.pi*frequency/c


