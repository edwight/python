import numpy as np
import matplotlib.pyplot as plt

# sample data
x = np.arange(10)
y = 5*x + 10 

# fit with np.polyfit
m, b = np.polyfit(x, y, 1)

plt.plot(x, y, '.', c='r')
plt.plot(x, m*x + b, '-')
plt.show()