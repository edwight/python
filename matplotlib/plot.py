import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
area = np.pi * (15 * np.random.rand(50))**2  # 0 to 15 point radii

fig = plt.figure()
ax1= fig.add_subplot(221)
ax2= fig.add_subplot(222)
ax3= fig.add_subplot(212)
ax1.hist(x, bins=15, normed=True, alpha=0.5)
ax2.plot(y, color='g', label = 'por defecto')
#ax2.suptitle('plot random')
ax3.scatter(x, y, c=colors, s=area, alpha=0.5)

plt.xlabel('valores x')
plt.show()

