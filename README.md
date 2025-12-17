# Omega-CDM
### A Late-Time Scalar–Tensor Framework for Growth Suppression

[![Status](https://img.shields.io/badge/Status-Research_Letter-blue)](https://github.com/)
[![Cosmology](https://img.shields.io/badge/Field-Late__Universe-purple)]()
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 🌌 Scientific Scope & Abstract

**Omega-CDM** is a phenomenological scalar–tensor framework designed to explore controlled late-time deviations from General Relativity. The primary goal is to address current tensions in large-scale structure growth (notably the **$S_8$ tension**) while preserving consistency with background cosmology and **DESI 2024** observations.

This repository provides:
* A self-consistent modification of the effective gravitational coupling $G_{\mathrm{eff}}(a)$.
* Numerical predictions for late-time observables such as $f\sigma_8(z)$.
* A dynamically evolving dark energy equation of state $w(z)$.
* Explicit control via a single coupling parameter $\beta$.

> **Note:** This work is presented as a **theoretical proposal and numerical forecast**. It focuses on the phenomenology at $z \lesssim 2.5$.

---

## 📊 Main Results (v1.0)

Based on the numerical implementation included in `Omega_solver.py`:

1.  **Controlled Suppression:**
    The model predicts a suppression of structure growth:
    $$\Delta f\sigma_8(z=1) \simeq -4.8\% \quad (\text{for } \beta = 0.4)$$
    This aligns with the requirements to alleviate the tension between Planck and weak lensing surveys (KiDS/DES).

2.  **GR Recovery:**
    The screening mechanism ensures strict recovery of General Relativity at $z=0$:
    $$G_{\mathrm{eff}}(z=0) \approx 1.00$$

3.  **Dynamic Dark Energy:**
    The scalar field supports a phantom-crossing equation of state $w(z)$, consistent with recent DESI hints.

---

## ⚙️ Model Parameters

The framework is controlled by the following effective parameters:

| Parameter | Symbol | Fiducial | Physical Role |
| :--- | :---: | :---: | :--- |
| **Disformal Coupling** | $\beta$ | `0.4` | Strength of the growth suppression (screening). |
| **Kinetic Scale** | $\alpha$ | `1.0` | Normalization of the kinetic term. |
| **Initial Velocity** | $\Omega'_0$ | `0.05` | Determines the redshift onset of the modification. |

---

## ⚠️ Limitations & Future Work

The current implementation focuses on **late-time phenomenology**. While numerically robust, the following components are scheduled for future development:

* **Global Statistical Validation:** A full MCMC likelihood analysis against Planck, BAO, and SNIa data has not yet been performed in this repository.
* **CMB Physics:** The impact on the full CMB angular power spectra ($C_\ell^{TT,TE}$) requires implementation in a Boltzmann solver (e.g., CLASS or CAMB).
* **Early Universe:** The model currently assumes a standard $\Lambda$CDM behavior at high redshifts ($z \gg 100$).

These limitations are consistent with the scope of a **Research Letter** or exploratory proposal.

---

## 📜 Citation

If you use this code or framework in your research, please cite as:

> **Helios Samuel**, *Omega-CDM Framework: Controlled Suppression of Structure Growth*, GitHub Repository, 2025.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
