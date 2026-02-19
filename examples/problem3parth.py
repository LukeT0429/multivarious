import numpy as np

# define the Hessian matrix H, vector c and the number d from part b
H = np.array([[ 24, -12,   3],
              [-12,  70, -18],
              [  3, -18,  36]])

c = np.array([10, -20, -26])
d = 151

# Define the Constraint components from part f
A = np.array([[-6,  4, -2],
              [ 7, -5,  3]])

b = np.array([-8, 9])

# Create the KKT Matrix
# [[H, A.T], [A, 0]]
top_block = np.hstack((H, A.T))
bottom_block = np.hstack((A, np.zeros((2, 2))))
KKT_matrix = np.vstack((top_block, bottom_block))

# Create the Right-Hand Side vector
# Vector structure: [-c, b]
RHS = np.concatenate((-c, b))

# Solve the linear system consisting of the kkt system = to rhs
sol = np.linalg.solve(KKT_matrix, RHS)

# Split the solution into v* and lambda*, the structure of the KKT system that was solved for
v_opt = sol[:3]
lambda_opt = sol[3:]

# Calculate the final objective function value f(v*) outlined in the problem
f_opt = 0.5 * v_opt.T @ H @ v_opt + c.T @ v_opt + d

# Output Results
print("Part (h) Results:")
print(f"Optimal variables (v*): {v_opt}")
print(f"Lagrange Multipliers (lambda*): {lambda_opt}")
print(f"Objective Function Value f(v*): {f_opt:.4f}")

# Confirmation check: Av - b should be zero or close to it
print(f"Constraint Check (Av - b): {A @ v_opt - b}")
