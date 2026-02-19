import sympy as sp

# Define symbols
v1, v2, v3 = sp.symbols('v1 v2 v3')

# Define Hessian matrix H and vector c
H = sp.Matrix([
    [24, -12,  3],
    [-12, 70, -18],
    [ 3, -18, 36]
])

c = sp.Matrix([10, -20, -26])

# Solve the linear system Hv + c = 0  →  v = -H^{-1} c
v_star = -H.LUsolve(c)

print("Optimal v*:")
print(v_star)

# Define the objective function
f = (12*v1**2 + 35*v2**2 + 18*v3**2
     - 12*v1*v2 + 3*v1*v3 - 18*v2*v3
     + 10*v1 - 20*v2 - 26*v3 + 151)

# Evaluate f at v*
f_star = f.subs({v1: v_star[0], v2: v_star[1], v3: v_star[2]})

print("\nMinimum value f(v*):")
print(sp.simplify(f_star))