import numpy as np
from multivarious.opt import ors, nms, sqp
from multivarious.utl import plot_cvg_hst

# Calculate objective series given in problem: f(v) = sum_{k=1}^n (1/k) * (v_k - k)^2
def udo_dimensionality_problem(v, C):
    # finds how many variables its working with from v
    n = len(v)
    # starts the algorithm at 0
    f = 0.0

    # evaluate given series from 1 to n plus 1
    for k in range(1, n + 1):
        f += (1.0 / k) * (v[k - 1] - k) ** 2

    # given value for g to prevent the constraint from ever binding the solution
    g = np.array([-1.0])

    return f, g


C = 1  # placeholder, not used

# Run optimization for different problem sizes
for n in [2, 10, 50]:

    print("\n" + "-" * 50)
    print(f"Running optimization for n = {n}")

    # Given bounds in problem: -2n <= v_k <= 2n
    v_lb = -2 * n * np.ones(n)
    v_ub =  2 * n * np.ones(n)

    # Initial guess
    v_init = np.zeros(n)

    # Optimization options
    #      msg    total_v     tol_f   tol_g   MaxIter  Penalty
    opts = [1, 1.0 / (v_ub[0] - v_lb[0]), 1e-3, 1e-4, 1000, 100]

    # Runs the optimization in nms, ors or sqp using previously calculated or entered values
    v_opt, f_opt, g_opt, cvg_hst, _, _ = \
        sqp(udo_dimensionality_problem, v_init, v_lb, v_ub, opts, C)

    # Can run with ors using: ors(udo_dimensionality_problem, v_init, v_lb, v_ub, opts, C)
    # Can run with sqp using: sqp(udo_dimensionality_problem, v_init, v_lb, v_ub, opts, C)

    print(f"Optimal f = {f_opt:.6f}")
    print(f"First five optimal variables: {v_opt[:5]}")

    plot_cvg_hst(cvg_hst, v_opt, opts, pdf_plots=True)