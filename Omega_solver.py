import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ---------------- PARAMETERS ----------------
OMEGA_M0 = 0.31
SIGMA8_0 = 0.8
ALPHA = 1.0
BETA = 0.25   # << SAFE CALIBRATED VALUE

# ---------------- BACKGROUND ----------------
def Omega_m(a):
    return OMEGA_M0 / (OMEGA_M0 + (1 - OMEGA_M0) * a**3)

def Omega_prime(a):
    return 0.05 * np.exp(-5*a)

def G_eff(a):
    return 1 - (2*BETA**2/ALPHA) * (Omega_prime(a)**2 / (1 + Omega_prime(a)**2))

# ---------------- GROWTH SYSTEM ----------------
def growth_eq(lna, y):
    delta, ddelta = y
    a = np.exp(lna)
    Om = Omega_m(a)
    Ge = G_eff(a)

    d2delta = -(2 - 1.5*Om)*ddelta + 1.5*Om*Ge*delta
    return [ddelta, d2delta]

# ---------------- INTEGRATION ----------------
lna_ini, lna_end = np.log(1e-3), 0.0
sol = solve_ivp(
    growth_eq,
    [lna_ini, lna_end],
    [1e-3, 1e-3],
    dense_output=True
)

lna = np.linspace(lna_ini, lna_end, 400)
a = np.exp(lna)
z = 1/a - 1

delta = sol.sol(lna)[0]
delta /= delta[-1]

f = sol.sol(lna)[1] / delta
fs8 = f * delta * SIGMA8_0

# ---------------- LCDM ----------------
fs8_lcdm = (Omega_m(a)**0.55) * delta * SIGMA8_0

# ---------------- METRICS ----------------
z1 = np.argmin(np.abs(z - 1.0))
supp = 100*(fs8[z1]/fs8_lcdm[z1] - 1)

gamma = np.log(f[-1]) / np.log(Omega_m(1.0))

print("---- Omega-CDM v1.1 Diagnostics ----")
print(f"Suppression at z=1: {supp:.2f}%")
print(f"G_eff(z=0) = {G_eff(1.0):.4f}")
print(f"Growth index gamma(z→0) ≈ {gamma:.3f}")

# ---------------- PLOT ----------------
plt.figure(figsize=(9,6))
plt.plot(z, fs8_lcdm, 'k--', label=r'$\Lambda$CDM')
plt.plot(z, fs8, 'b', lw=2, label=fr'Omega-CDM ($\beta={BETA}$)')
plt.xlim(0,2)
plt.xlabel('Redshift $z$')
plt.ylabel(r'$f\sigma_8(z)$')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
