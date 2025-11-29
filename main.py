import numpy as np

import matplotlib.pyplot as plt

# Generate x values from -2π to 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calculate sin(x)
y = np.sin(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2, label='sin(x)')
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Function')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.legend()
plt.show()