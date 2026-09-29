# Mathematical Modelling of Malaria Transmission

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active_research-brightgreen)

A computational framework for studying malaria transmission dynamics under mosquito population replacement strategies and climate variability.

## Research Question

How can mathematical models be used to investigate mosquito population replacement strategies (e.g., *Wolbachia* introgression) for reducing malaria transmission, and what is the optimal release strategy under climate forcing?

## Objectives

1. Develop a deterministic transmission model coupling human SEIR and vector SEI dynamics.
2. Derive the basic reproduction number ($R_0$) using the Next-Generation Matrix approach.
3. Analyse disease-free and endemic equilibria for stability.
4. Perform numerical simulations to visualize epidemic trajectories.
5. Investigate parameter sensitivity via Latin Hypercube Sampling (LHS) and Partial Rank Correlation Coefficient (PRCC).
6. Introduce climate-dependent parameters (e.g., seasonal mosquito birth rates).
7. Evaluate intervention strategies using optimal control theory.

## Mathematical Framework

The core transmission dynamics are governed by a coupled system of nonlinear ordinary differential equations. The human population follows an SEIR structure, while the vector population follows an SEI structure with an additional compartment ($W$) for the replacement mosquito population.

### Human Population Dynamics
$$\frac{dS_h}{dt} = \Lambda_h - \frac{b \beta_{hv} S_h I_v}{N_h} - \mu_h S_h$$
$$\frac{dE_h}{dt} = \frac{b \beta_{hv} S_h I_v}{N_h} - (\nu_h + \mu_h) E_h$$
$$\frac{dI_h}{dt} = \nu_h E_h - (\gamma_h + \mu_h + \delta_h) I_h$$
$$\frac{dR_h}{dt} = \gamma_h I_h - \mu_h R_h$$

### Vector Population Dynamics (Wild-Type & Replacement)
$$\frac{dS_v}{dt} = \Lambda_v - \frac{b \beta_{vh} S_v I_h}{N_h} - \mu_v S_v - c S_v W$$
$$\frac{dE_v}{dt} = \frac{b \beta_{vh} S_v I_h}{N_h} - (\nu_v + \mu_v) E_v$$
$$\frac{dI_v}{dt} = \nu_v E_v - \mu_v I_v$$
$$\frac{dW}{dt} = u(t) + \Lambda_w - \mu_w W + c S_v W$$

*(Where u(t) represents the time-dependent control variable for releasing modified mosquitoes, and c is the competition coefficient).*

## Computational Methods

This project relies on a modular modeling ecosystem. The core solvers are imported from our proprietary `ode-modeling-toolkit`.

* **Symbolic Computation:** `SymPy` for automated $R_0$ derivation.
* **Numerical Integration:** `SciPy` (`solve_ivp`) for ODE evaluation.
* **Data Processing & Analytics:** `NumPy`, `Pandas`.
* **Visualization:** `Matplotlib` and `Seaborn` for phase portraits and time-series curves.

## Reproducibility

*(Instructions for cloning the repository and running the simulation scripts will be added as the codebase is populated).*

## Author
**Quadri Ayodeji Ajadi**
