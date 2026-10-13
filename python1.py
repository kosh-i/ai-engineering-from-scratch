import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Plot
plt.plot(x, y, label="sin(x)")
plt.title("Matplotlib Test Plot")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()

# Show the plot window
plt.show()
