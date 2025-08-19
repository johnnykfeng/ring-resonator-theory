# Ring Resonator Theory

This project provides an interactive demo and a set of utility functions for exploring the transmission properties and resonance conditions of optical ring resonators. It is intended for students, researchers, and engineers interested in photonics, integrated optics, or related fields.

## Features

- **Interactive Streamlit App**: Visualize the transmission spectrum of a ring resonator as a function of wavelength. Adjust parameters in real time and see the effect on resonance and transmission.
- **Analytical Equations**: Core equations for ring resonator transmission, resonance wavelengths, and conversions between wavelength, frequency, and wavenumber.
- **Modular Code**: All equations are provided in a reusable Python module.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Running the Streamlit App](#running-the-streamlit-app)
  - [Using the Equations Module](#using-the-equations-module)
- [Project Structure](#project-structure)
- [Equations Reference](#equations-reference)
- [License](#license)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ring-resonator-theory.git
   cd ring-resonator-theory
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment.
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
   Or, if you use [Poetry](https://python-poetry.org/) or another tool, install from `pyproject.toml`.

   **Dependencies:**
   - numpy
   - matplotlib
   - streamlit

---

## Usage

### Running the Streamlit App

The main interactive demo is in `app.py`. To launch the app:
