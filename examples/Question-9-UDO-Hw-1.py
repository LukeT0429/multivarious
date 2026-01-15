import numpy as np
import matplotlib.pyplot as plt

# dimensionless load location
x = np.linspace(0, 1, 100)   # x = a/L

# dimensionless end rotation (one line, no for-loop)
theta_bar = 0.5 * x * (1 - x**2)

# find maximum using argmax
i_max = np.argmax(theta_bar)
x_max = x[i_max]
theta_max = theta_bar[i_max]

# plot
plt.plot(x, theta_bar)
plt.plot(x_max, theta_max, 'ro')
plt.xlabel('a / L')
plt.ylabel('EIθ₂ / (F L²)')
plt.title('Dimensionless End Rotation vs Load Location')
plt.grid(True)
plt.show()