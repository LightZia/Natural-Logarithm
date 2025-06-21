import matplotlib
matplotlib.use('TkAgg')  # Force a GUI backend

import matplotlib.pyplot as plt
import numpy as np

# Number of compounding intervals
n = np.linspace(1, 1000, 1000)
compound_values = (1 + 1/n)**n

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(n, compound_values, label=r'$\left(1 + \frac{1}{n} \right)^n$', color='blue')
plt.axhline(y=np.exp(1), color='red', linestyle='--', label=r'$e \approx 2.71828$')
plt.title('Approaching the Number $e$ through Compound Interest')
plt.xlabel('Number of Compounding Intervals per Year (n)')
plt.ylabel('Final Amount after 1 Year')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
