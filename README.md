# Omega-CDM Framework (v1.1)

![Status](https://img.shields.io/badge/Status-Calibrated_Numerical_Implementation-success)
![Field](https://img.shields.io/badge/Field-Cosmology%20%7C%20Modified_Gravity-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**A late-time scalar–tensor framework for controlled suppression of structure growth.**

---

## 📊 Visual Summary: Growth Suppression

![Omega-CDM v1.1 Growth Suppression](omega_v1p1_plot.png)

**Figure 1 —** Prediction of the growth observable \( f\sigma_8(z) \) in **Omega-CDM (v1.1)** compared to standard **ΛCDM**.  
The Omega-CDM model (blue, \( \beta = 0.25 \)) exhibits a controlled suppression at intermediate redshifts  
\( 0.5 \lesssim z \lesssim 1.5 \), while recovering General Relativity at \( z = 0 \).

---

## 🔭 Scientific Scope

**Omega-CDM** is a phenomenological scalar–tensor framework designed to explore **late-time deviations from General Relativity** with the explicit goal of alleviating the **\( S_8 \) tension** between CMB measurements (Planck) and large-scale structure probes (KiDS/DES/DESI).

The framework is intentionally restricted to:
- Linear perturbations  
- Quasi-static regime  
- Late cosmological times \( (z \lesssim 2.5) \)

This repository is **not** a full Boltzmann-solver implementation, but a **calibrated numerical forecast** suitable for research-letter–level studies.

---

## 📈 Main Results (v1.1 — Calibrated)

Based on the full second-order numerical integration implemented in `Omega_solver.py`:

1. **Controlled Growth Suppression**  
   \[
   \Delta f\sigma_8(z=1) \simeq -5\% \; \text{to} \; -8\%
   \]
   consistent with the level required to relieve the \( S_8 \) tension without violating current RSD constraints.

2. **Modified Gravity Signature**  
   The effective late-time growth index satisfies:
   \[
   \gamma(z \to 0) \approx 0.63
   \]
   clearly deviating from the General Relativity prediction \( \gamma \approx 0.55 \).

3. **Recovery of General Relativity**  
   The screening mechanism ensures:
   \[
   G_{\mathrm{eff}}(z=0) \approx 1
   \]
   maintaining consistency with Solar System and local gravity tests.

---

## ⚙️ Model Parameters (v1.1)

| Parameter | Symbol | Fiducial Value | Physical Role |
|---------|--------|----------------|---------------|
| Disformal coupling | \( \beta \) | **0.25** | Strength of late-time growth suppression |
| Kinetic normalization | \( \alpha \) | 1.0 | Scalar kinetic scale |
| Matter density | \( \Omega_{m0} \) | 0.31 | Planck-consistent background |
| Amplitude | \( \sigma_{8,0} \) | 0.8 | Growth normalization |

> **Note:** Earlier versions using approximate solvers required recalibration.  
> Version **v1.1** uses a full second-order integration (`solve_ivp`), providing higher numerical fidelity.

---

## 🚀 Quick Start

To reproduce the results and the main figure:

```bash
git clone https://github.com/heliossamuelhernandezreyes/Omega-CDM-A-Late-Time-Scalar-Tensor-Framework-for-Growth-Suppression
cd Omega-CDM-A-Late-Time-Scalar-Tensor-Framework-for-Growth-Suppression
pip install -r requirements.txt
python Omega_solver.py
