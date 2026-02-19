import time
from datetime import datetime, timedelta

import numpy as np
from numpy import pi, sin, cos, exp

from multivarious.opt import ors
from multivarious.opt import nms
from multivarious.opt import sqp
from multivarious.utl import plot_cvg_hst


# ============================================================
# HW 2 – Problem 7(a)
# Analysis function
# ============================================================

def udo_HW2P7_2026_analysis(v, C):
    """
    Evaluate objective f(v) and constraints g(v)
    """

    v1 = v[0]
    v2 = v[1]
    v3 = v[2]

    ss = v1**2 + v2**2 + v3**2

    # Objective
    f = ss + 103.0 * exp(-ss)

    # Constraints (must be <= 0)
    g1 = 0.5 + cos(pi * v1 / 4.0)
    g2 = 0.5 + sin(pi * v2 / 3.0)

    g = np.array([g1, g2])

    return f, g


# ============================================================
# Problem setup
# ============================================================

C = 1  # placeholder, not used

v_lb = np.array([-10.0, -10.0, -10.0])
v_ub = np.array([ 10.0,  10.0,  10.0])

increment = 0.1

# ============================================================
# HW 2 – Problem 7(c)
# ORS, NMS, SQP (TABLE DATA)
# ============================================================

# Initial conditions required by the table
initial_conditions = [
    np.array([5.0, 0.0, 0.0]),
    np.array([0.0, 5.0, 0.0]),
    np.array([0.0, 0.0, 2.0])
]

# msg, tol_v, tol_f, tol_g, max_iter, penalty
opts = [1, increment/(v_ub[0]-v_lb[0]), 1e-2, 1e-4, 1000, 100]

methods = [
    ("ors", ors),
    ("nms", nms),
    ("sqp", sqp)
]

print("\n================ HW2 PROBLEM 7(c) RESULTS =================\n")

for method_name, method in methods:
    for v_init in initial_conditions:

        v_opt, f_opt, g_opt, cvg_hst, n_eval, _ = method(
            udo_HW2P7_2026_analysis,
            v_init,
            v_lb,
            v_ub,
            opts,
            C
        )

        g1_star = g_opt[0]
        g2_star = g_opt[1]

        # Identify binding constraints (what you circle)
        bind_g1 = abs(g1_star) < 1e-4
        bind_g2 = abs(g2_star) < 1e-4

        print(f"method      : {method_name}")
        print(f"v_init      : {v_init}")
        print(f"f*          : {f_opt:.6f}")
        print(f"g1*         : {g1_star:.6e} {'<-- binding' if bind_g1 else ''}")
        print(f"g2*         : {g2_star:.6e} {'<-- binding' if bind_g2 else ''}")
        print(f"v*          : {v_opt}")
        print(f"analyses    : {n_eval}")
        print("-" * 70)

        # Optional: convergence plots
        plot_cvg_hst(cvg_hst, v_opt, opts, pdf_plots=True)