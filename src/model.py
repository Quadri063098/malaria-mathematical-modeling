import sys
import os
from typing import List

# Allow local import of the toolkit from the sibling directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ode-modeling-toolkit')))
from ode_toolkit.base_model import BaseODEModel

class MalariaReplacementModel(BaseODEModel):
    """
    Coupled human-vector malaria transmission model incorporating a 
    Wolbachia mosquito replacement compartment (W).
    
    State Variables (y):
    [Sh, Eh, Ih, Rh, Sv, Ev, Iv, W]
    """
    def equations(self, t: float, y: List[float]) -> List[float]:
        # Unpack state variables for readability
        Sh, Eh, Ih, Rh, Sv, Ev, Iv, W = y
        
        # Calculate total human population (Nh) dynamically
        Nh = Sh + Eh + Ih + Rh
        
        # Prevent division by zero in case of population collapse
        if Nh <= 0:
            Nh = 1e-9
            
        # Bind parameters to a local variable for cleaner syntax
        p = self.params
        
        # Force of infection (lambda)
        # b: biting rate, beta_hv: vector-to-human transmission, beta_vh: human-to-vector
        lambda_h = (p['b'] * p['beta_hv'] * Iv) / Nh
        lambda_v = (p['b'] * p['beta_vh'] * Ih) / Nh
        
        # Time-dependent control function for Wolbachia release
        # If 'u' is provided as a static parameter, use it; otherwise default to 0.
        u_release = p.get('u', 0.0) 

        # --- Human Population Dynamics (SEIR) ---
        dSh = p['Lambda_h'] - lambda_h * Sh - p['mu_h'] * Sh
        dEh = lambda_h * Sh - (p['nu_h'] + p['mu_h']) * Eh
        dIh = p['nu_h'] * Eh - (p['gamma_h'] + p['mu_h'] + p['delta_h']) * Ih
        dRh = p['gamma_h'] * Ih - p['mu_h'] * Rh
        
        # --- Vector Population Dynamics (SEI + W) ---
        dSv = p['Lambda_v'] - lambda_v * Sv - p['mu_v'] * Sv - p['c'] * Sv * W
        dEv = lambda_v * Sv - (p['nu_v'] + p['mu_v']) * Ev
        dIv = p['nu_v'] * Ev - p['mu_v'] * Iv
        dW  = u_release + p['Lambda_w'] - p['mu_w'] * W + p['c'] * Sv * W
        
        return [dSh, dEh, dIh, dRh, dSv, dEv, dIv, dW]