import numpy as np
import matplotlib.pyplot as plt
from multivarious.ode import ode4u

def ball_flight_dyn(t, x, u, c):
    """
    ODE function for ball flight with backspin.
    """

    # Unpack state
    px = x[0]
    py = x[1]
    vx = x[2]
    vy = x[3]

    # Unpack constants
    g, r, m, rho, omega, CD, CL = c

    # Unit vector in y-direction
    j = np.array([0.0, 1.0, 0.0])

    # Velocity vector (3D)
    v = np.array([vx, vy, 0.0])

    # Backspin vector
    w = np.array([0.0, 0.0, omega])

    # -------------------------
    # Forces
    # -------------------------

    # Gravity
    fG = -m * g * j

    # Drag
    fD = -CD * (np.pi * r**2) * (0.5 * rho * np.linalg.norm(v) * v)

    # Lift (Magnus force)
    fL = CL * (16.0/3.0) * (np.pi**2) * r**3 * rho * np.cross(w, v)

    # Net force
    f = fG + fD + fL

    # -------------------------
    # State derivatives
    # -------------------------
    dxdt = np.array([
        vx,              # d(px)/dt
        vy,              # d(py)/dt
        f[0] / m,        # d(vx)/dt
        f[1] / m         # d(vy)/dt
    ])

    # Output force magnitudes (optional)
    y = np.array([
        np.linalg.norm(fG),
        np.linalg.norm(fD),
        np.linalg.norm(fL)
    ])

    return dxdt, y


# ===============================
# Simulation Code (from template)
# ===============================

# Constants
g = 9.806                  # gravitational acceleration (m/s^2)
r = 0.12                   # radius of basketball (m)
m = 0.62                   # mass of basketball (kg)
rho = 1.2                  # air density (kg/m^3)
omega = 8 * np.pi          # backspin angular velocity (rad/s)
CD = 0.47                  # drag coefficient
CL = 0.2                   # lift coefficient

c = (g, r, m, rho, omega, CD, CL)

# Time parameters
T = 8.0                    # total simulation time (s)
dt = 0.01                  # time step (s)
nT = int(np.floor(T / dt))
t_eval = np.linspace(0, T, nT)

# Initial state: [px, py, vx, vy]
x0 = np.array([0.0, 2.0, 8.0, 6.0])

# External forcing (not used)
u = np.zeros((1, nT))

# Solve ODE
time, x, _, _ = ode4u(ball_flight_dyn, t_eval, x0, u, c)

# Extract position
px = x[0, :]
py = x[1, :]

# Plot trajectory
plt.figure(1)
plt.clf()
plt.plot(px, py, label='Trajectory')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.title('Ball Flight Trajectory with Backspin')
plt.legend()
plt.grid(True)
plt.show()