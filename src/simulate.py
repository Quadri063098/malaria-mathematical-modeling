import sys
import os
import numpy as np

# Allow local import of the toolkit from the sibling directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ode-modeling-toolkit')))

from ode_toolkit.plotting import plot_time_series
from model import MalariaReplacementModel

def main():
    # 1. Define Epidemiological Parameters
    # (Values are placeholder approximations for demonstration)
    parameters = {
        # Human Parameters
        'Lambda_h': 10.0,    # Human recruitment/birth rate
        'mu_h': 0.00004,     # Human natural death rate (approx. 1/(70 years in days))
        'nu_h': 0.1,         # Rate of progression from Exposed to Infected (human)
        'gamma_h': 0.05,     # Recovery rate
        'delta_h': 0.001,    # Disease-induced death rate
        
        # Transmission Parameters
        'b': 0.5,            # Mosquito biting rate
        'beta_hv': 0.3,      # Transmission probability (vector to human)
        'beta_vh': 0.4,      # Transmission probability (human to vector)
        
        # Vector Parameters
        'Lambda_v': 1000.0,  # Wild-type vector recruitment rate
        'mu_v': 0.07,        # Vector natural death rate (approx. 1/(14 days))
        'nu_v': 0.08,        # Rate of progression from Exposed to Infected (vector)
        
        # Wolbachia / Replacement Parameters
        'Lambda_w': 200.0,   # Baseline recruitment of modified mosquitoes
        'mu_w': 0.08,        # Natural death rate of modified mosquitoes
        'c': 0.0001,         # Competition coefficient between vector types
        'u': 50.0            # Constant daily release rate of Wolbachia mosquitoes (Intervention)
    }

    # 2. Define Initial Conditions
    # Order: [Sh, Eh, Ih, Rh, Sv, Ev, Iv, W]
    initial_states = [
        10000.0,  # Sh: 10,000 susceptible humans
        0.0,      # Eh: 0 exposed humans
        100.0,    # Ih: 100 infected humans (seed of the outbreak)
        0.0,      # Rh: 0 recovered humans
        50000.0,  # Sv: 50,000 susceptible wild mosquitoes
        0.0,      # Ev: 0 exposed mosquitoes
        500.0,    # Iv: 500 infected mosquitoes
        0.0       # W: 0 Wolbachia mosquitoes initially
    ]

    # 3. Time Span (Simulate for 365 days)
    t_span = (0, 365)
    t_eval = np.linspace(t_span[0], t_span[1], 1000)

    # 4. Initialize and Solve the Model
    print("Initializing Malaria Replacement Model...")
    malaria_model = MalariaReplacementModel(parameters, initial_states)
    
    print("Solving the ODE system...")
    solution = malaria_model.solve(t_span=t_span, t_eval=t_eval)

    # 5. Plot the Results using the ODE Toolkit
    print("Generating epidemic curves...")
    labels = ['S_h (Susceptible Humans)', 'E_h (Exposed Humans)', 
              'I_h (Infected Humans)', 'R_h (Recovered Humans)',
              'S_v (Susceptible Vectors)', 'E_v (Exposed Vectors)', 
              'I_v (Infected Vectors)', 'W (Wolbachia Vectors)']
    
    plot_time_series(
        solution=solution,
        labels=labels,
        title="Malaria Transmission Dynamics with Wolbachia Intervention",
        xlabel="Time (Days)",
        ylabel="Population Size"
    )

if __name__ == "__main__":
    main()