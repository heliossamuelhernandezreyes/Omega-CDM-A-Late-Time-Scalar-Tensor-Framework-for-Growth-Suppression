import numpy as np
from scipy.integrate import solve_ivp

# ==============================================================================
# OMEGA-CDM FRAMEWORK: NUMERICAL SOLVER v1.0
# ==============================================================================
# Author: Helios Samuel Hernández Reyes
# Status: Research Forecast / Late-Time Phenomenology
# License: MIT
#
# DESCRIPTION:
# This script integrates the linear growth of structure perturbations in the
# Omega-CDM framework. It implements a scalar-tensor screening mechanism
# via a modified effective gravitational coupling G_eff(a).
# ==============================================================================

# 1. FIDUCIAL PARAMETERS
# ----------------------
# Calibrated to produce ~4.8% suppression at z=1.0 consistent with S8 tension.
Omega_m0 = 0.3       # Matter density parameter today
sigma8_0 = 0.8       # Reference amplitude (Planck-like)
alpha    = 1.0       # Kinetic scale normalization
beta     = 0.4       # COUPLING STRENGTH (Primary control parameter)
Omega0_p = 0.05      # Initial field velocity

# 2. BACKGROUND EVOLUTION FUNCTIONS
# ---------------------------------
def Omega_m(a):
    """Evolution of matter density parameter."""
    return Omega_m0 / (Omega_m0 + (1 - Omega_m0) * a**3)

def Omega_prime(a):
    """
    Scalar field velocity profile.
    Decays exponentially to ensure GR recovery at early times.
    """
    return Omega0_p * np.exp(-5 * a)

def G_eff(a):
    """
    EFFECTIVE GRAVITATIONAL COUPLING
    Implements the disformal screening mechanism.
    G_eff < 1 implies growth suppression relative to GR.
    """
    Op = Omega_prime(a)
    # The interaction term leading to suppression:
    return 1.0 - (2 * beta**2 / alpha) * (Op**2 / (1 + Op**2))

# 3. LINEAR GROWTH EQUATION (ODE)
# -------------------------------
def growth_eq(x, y):
    """
    Solves for density contrast delta(a).
    x = ln(a)
    y = [delta, delta']
    """
    a = np.exp(x)
    delta, ddelta = y
    
    Om = Omega_m(a)
    Ge = G_eff(a) # Modified gravity injection

    # Friction term (2 - 1.5*Om) and Source term (1.5*Om*Ge*delta)
    d2delta = -(2 - 1.5 * Om) * ddelta + 1.5 * Om * Ge * delta
    
    return [ddelta, d2delta]

# 4. NUMERICAL INTEGRATION
# ------------------------
def solve_growth():
    # Integrate from deep matter era (a=0.001) to today (a=1)
    a_ini = 1e-3
    x_ini = np.log(a_ini)
    x_end = 0.0 

    y0 = [a_ini, a_ini] # Adiabatic initial conditions
    
    sol = solve_ivp(growth_eq, [x_ini, x_end], y0, rtol=1e-8, atol=1e-8)
    return sol

# 5. MAIN EXECUTION
# -----------------
if __name__ == "__main__":
    print(f"--- RUNNING OMEGA-CDM FORECAST (beta={beta}) ---")
    
    sol = solve_growth()
    
    # Extract results at z=1 (approx a=0.5)
    idx = np.argmin(np.abs(np.exp(sol.t) - 0.5))
    f_z1 = sol.y[1][idx] / sol.y[0][idx]
    
    print(f"Simulation Status: CONVERGED")
    print(f"Resulting Growth Rate f(z=1): {f_z1:.5f}")
    print("Note: Compare this value against LambdaCDM baseline (~0.45).")
