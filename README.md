# Mathematical Modelling of Malaria Transmission and Vector Population Replacement

## Overview

This project develops a computational mathematical framework for investigating malaria transmission and the potential use of mosquito population replacement as a disease-control strategy.

The work combines **mathematical epidemiology, dynamical systems, numerical analysis, and scientific computing** to study interactions between human and mosquito populations and to investigate how changes in vector population dynamics may affect malaria transmission.

The project is part of an independent research portfolio focused on applying mathematical and computational methods to biological and public-health problems.

---

## Research Question

**How can mathematical models be used to investigate the effect of mosquito population replacement on malaria transmission dynamics?**

The project is motivated by the need to understand malaria-control strategies beyond conventional vector reduction, particularly approaches that alter the composition or transmission competence of mosquito populations.

---

## Research Objectives

The project aims to:

1. Formulate a deterministic compartmental model for malaria transmission.
2. Represent interactions between human and mosquito populations mathematically.
3. Establish the mathematical properties of the model.
4. Derive and analyse the basic reproduction number, \(R_0\).
5. Investigate disease-free and endemic equilibria.
6. Perform numerical simulations of transmission dynamics.
7. Examine the sensitivity of model behaviour to key parameters.
8. Investigate how environmental or climate-dependent parameters may influence transmission.
9. Explore intervention strategies through mathematical and computational analysis.

---

## Mathematical Framework

The model is formulated using a system of ordinary differential equations.

The human population is divided into epidemiological compartments, while the mosquito population is represented according to its relevant infection or transmission states.

A general representation is

$$
\frac{d\mathbf{x}}{dt} = \mathbf{F}(\mathbf{x},\theta,t),
$$

where

* \(\mathbf{x}\) represents the population-state variables,
* \(\theta\) represents model parameters,
* \(t\) represents time.

The exact compartment definitions, assumptions, parameter values, and governing equations are documented in the model documentation.

---

## Mathematical Analysis

The analytical component of the project focuses on:

### Basic Reproduction Number

The basic reproduction number \(R_0\) is derived using the appropriate epidemiological framework and is used to investigate conditions associated with disease invasion and persistence.

### Equilibria

The project considers:

* Disease-free equilibrium
* Endemic equilibrium

where mathematically appropriate.

### Stability

Local stability properties are investigated using analytical and/or numerical methods.

### Sensitivity Analysis

Sensitivity analysis is used to identify parameters that have substantial influence on transmission dynamics and model outcomes.

---

## Computational Methods

The computational implementation uses Python-based scientific-computing tools.

### Main technologies

* Python
* NumPy
* SciPy
* Pandas
* Matplotlib
* Jupyter

Numerical methods are used to solve the governing differential equations and investigate model behaviour under different parameter configurations.

---

## Project Structure

```text
malaria-mathematical-modeling/
│
├── README.md
├── src/
├── notebooks/
├── analysis/
├── figures/
├── data/
├── tests/
├── docs/
├── requirements.txt
└── LICENSE
```

---

## Reproducibility

The project is maintained using Git and GitHub to support reproducible computational research.

To reproduce the computational experiments:

```bash
git clone https://github.com/Quadri-Ayo/malaria-mathematical-modeling.git
cd malaria-mathematical-modeling
pip install -r requirements.txt
```

Detailed instructions for individual experiments are provided in the relevant notebooks and documentation.

---

## Research Outputs

Results will be presented through:

* mathematical derivations,
* numerical simulations,
* parameter-sensitivity plots,
* equilibrium analysis,
* comparative intervention scenarios,
* and reproducible computational experiments.

Figures included in this repository are generated from the underlying model implementation.

---

## Limitations

The model represents a mathematical abstraction of a complex biological system. Consequently, model predictions depend on assumptions concerning population structure, parameter values, transmission mechanisms, and environmental conditions.

The results should therefore be interpreted as model-based insights rather than direct predictions of malaria incidence in a specific population.

---

## Future Work

Potential extensions include:

* stochastic formulations,
* spatially explicit models,
* climate-driven transmission parameters,
* uncertainty quantification,
* optimal control,
* parameter estimation using observational data,
* and comparison of alternative vector-control strategies.

---

## Research Context

This repository forms part of an independent research portfolio exploring the use of **mathematical modelling and computational methods in mathematical biology and epidemiology**.

The broader objective is to develop rigorous mathematical approaches for understanding complex biological systems and supporting evidence-based disease-control research.

---

## References

Relevant literature used in developing the mathematical formulation, epidemiological assumptions, and analytical methodology is documented in the project references.

> **Status:** Active independent research project.
