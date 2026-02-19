import numpy as np

from multivarious.opt import ors
from multivarious.opt import nms
from multivarious.opt import sqp
from multivarious.utl import plot_cvg_hst
# ==========================================
# Analysis function (dimension = len(v))
# ==========================================
def analysis(v, C):
    n = len(v)
    f = 0.0
    for k in range(n):
        f += (v[k] - (k+1))**2 / (k+1)

    g = np.array([-1.0])  # unconstrained
    return f, g


# ==========================================
# Run study
# ==========================================
for n in [2, 10, 50]:

    v_lb = -2*n * np.ones(n)
    v_ub =  2*n * np.ones(n)
    v_init = np.zeros(n)

    opts = [0, 1e-3, 1e-6, 1e-6, 2000, 100]

    print(f"\n===== n = {n} =====")

    for name, method in [("ORS", ors), ("NMS", nms), ("SQP", sqp)]:
        v_opt, f_opt, g_opt, _, n_eval, _ = method(
    analysis, v_init, v_lb, v_ub, opts, None
)
        print(f"{name}: f* = {f_opt:.3e}, analyses = {n_eval}")