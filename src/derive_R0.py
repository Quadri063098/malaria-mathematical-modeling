import sympy as sp

def main():
    print("--- Deriving R0 via Next-Generation Matrix ---")
    
    # 1. Define Symbolic Parameters
    b, beta_hv, beta_vh = sp.symbols('b beta_hv beta_vh', positive=True)
    mu_h, nu_h, gamma_h, delta_h = sp.symbols('mu_h nu_h gamma_h delta_h', positive=True)
    mu_v, nu_v = sp.symbols('mu_v nu_v', positive=True)
    Nh, Sv_star = sp.symbols('N_h S_v^*', positive=True) # Populations at Disease-Free Equilibrium

    # 2. Define Infected Compartments
    Eh, Ih, Ev, Iv = sp.symbols('E_h I_h E_v I_v')
    infected_states = sp.Matrix([Eh, Ih, Ev, Iv])

    # 3. Define F (Matrix of New Infections)
    # At the disease-free equilibrium (DFE), S_h approx N_h, so S_h/N_h = 1
    F_eq = sp.Matrix([
        b * beta_hv * Iv,                   # New exposed humans
        0,                                  # Ih (internal transition)
        (b * beta_vh * Sv_star / Nh) * Ih,  # New exposed vectors
        0                                   # Iv (internal transition)
    ])

    # 4. Define V (Matrix of Transitions) 
    # V = (Transitions OUT) - (Transitions IN excluding new infections)
    V_eq = sp.Matrix([
        (nu_h + mu_h) * Eh,
        (gamma_h + mu_h + delta_h) * Ih - nu_h * Eh,
        (nu_v + mu_v) * Ev,
        mu_v * Iv - nu_v * Ev
    ])

    # 5. Compute Jacobians evaluated at DFE
    F = F_eq.jacobian(infected_states)
    V = V_eq.jacobian(infected_states)

    print("\nJacobian F (New Infections Rate):")
    sp.pprint(F)
    
    print("\nJacobian V (Transition Rate):")
    sp.pprint(V)

    # 6. Compute V inverse and the Next Generation Matrix (K = F * V^-1)
    V_inv = V.inv()
    K = F * V_inv
    
    print("\nNext-Generation Matrix (K = F * V^-1):")
    sp.pprint(sp.simplify(K))

    # 7. Find Eigenvalues to get the Spectral Radius (R0)
    print("\nCalculating Eigenvalues (This may take a moment)...")
    eigenvals = K.eigenvals()
    
    for ev in eigenvals.keys():
        if ev != 0:
            print("\nSpectral Radius (R0):")
            # Because R0^2 is often what is returned for bipartite networks like Malaria
            sp.pprint(sp.simplify(ev))
            print("\n(Note: For coupled human-vector models, the true R0 is often the square root of this value).")

if __name__ == "__main__":
    main()