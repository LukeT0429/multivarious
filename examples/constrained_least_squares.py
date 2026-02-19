"""
CEE 251L Duke University
Example of constrained least squares curve fitting
Revised for specified basis functions and constraints
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, exp

interactive = True        # Enable interactive mode for matplotlib

# Values of independent variables, t1..tM
t_init = 0
t_finl = 10
delt_t = 0.10
t = np.arange(t_init, t_finl + delt_t, delt_t)

# Pre-selected latent values for the "true" coefficient
c_true = np.array([1, 0.5, 4, 5, -15])

n = len(c_true)   # number of coefficients
M = len(t)        # number of measured data points

# Basis matrix
B = np.column_stack([
    np.ones(M),
    t**2,
    sin(2*pi*t),
    cos(pi*t),
    exp(-t**2)
])

y_true = B @ c_true   # "true" values of y

# ---------------------------------------------------------
# Constraints
# ---------------------------------------------------------
# y(0) = 9
# y'(0) = 56
# y(10) = 35

tc1 = 0
tc2 = 10

# Constraint matrix A
A = np.array([
    [1, tc1**2, sin(2*pi*tc1), cos(pi*tc1), exp(-tc1**2)],                 # y(0)
    [0, 2*tc1, 2*pi*cos(2*pi*tc1), -pi*sin(pi*tc1), -2*tc1*exp(-tc1**2)],  # y'(0)
    [1, tc2**2, sin(2*pi*tc2), cos(pi*tc2), exp(-tc2**2)]                  # y(10)
])

b = np.array([9, 56, 35])

print(f'b = {b}')

# ---------------------------------------------------------
# Simulated noisy measurements
# ---------------------------------------------------------
np.random.seed(1)
y_meas = y_true + 10.0 * np.random.randn(M)

# ---------------------------------------------------------
# Unconstrained least squares fit
# ---------------------------------------------------------
c_fit_u = np.linalg.solve(B.T @ B, B.T @ y_meas)
y_hat_u = B @ c_fit_u

# ---------------------------------------------------------
# Constrained least squares fit (KKT system)
# ---------------------------------------------------------
KKT = np.block([
    [2 * B.T @ B, A.T],
    [A, np.zeros((3, 3))]
])

rhs = np.block([2 * B.T @ y_meas, b])

c_fit_c_lambda = np.linalg.solve(KKT, rhs)
c_fit_c = c_fit_c_lambda[:n]
y_hat_c = B @ c_fit_c

# ---------------------------------------------------------
# Error analysis
# ---------------------------------------------------------
err_u = y_hat_u - y_true
err_c = y_hat_c - y_true

RMSE_u = np.sqrt(err_u @ err_u / len(err_u))
RMSE_c = np.sqrt(err_c @ err_c / len(err_c))

# ---------------------------------------------------------
# Display results
# ---------------------------------------------------------
np.set_printoptions(precision=3, suppress=True)

print('\n   true     unconstrained   constrained')
print(np.column_stack([c_true, c_fit_u, c_fit_c]))

print('\n')
print(f' RMS (unconstrained - true) = {RMSE_u:.3f}')
print(f' RMS (  constrained - true) = {RMSE_c:.3f}')

# ---------------------------------------------------------
# Plot the results
# ---------------------------------------------------------
if interactive:
    plt.ion()

plt.figure(1, figsize=(8, 6))
plt.clf()
plt.plot(t, y_true, '-m', linewidth=3, label='latent (true)')
plt.plot(t, y_meas, 'ok', markerfacecolor='none', markersize=5,
         label='measurements')
plt.plot(t, y_hat_u, '--b', linewidth=3, label='unconstrained fit')
plt.plot(t, y_hat_c, '-g', linewidth=3, label='constrained fit')

plt.xlabel('independent variable, $t$', fontsize=15)
plt.ylabel('dependent variable, $y$', fontsize=15)
plt.legend(loc='lower right', fontsize=12)
plt.tick_params(labelsize=12)
plt.tight_layout()
plt.draw()
plt.pause(0.001)

# Save figure
filename = 'constrained-least-squares.pdf'
plt.savefig(filename, bbox_inches='tight', dpi=300)
print(f"\nSaved: {filename}")

# Exit
if interactive:
    input("Press Enter to close all figures ... ")
    plt.close('all')