#temperatura 
import numpy as np
import matplotlib.pyplot as plt


def leerTemperatura():
	tem = []
	for x in range(1,10):
		tem.append(np.random.rand(1))

	fig = plt.figure('temperaturas')
	ax1 = fig.add_subplot(221)
	ax1.plot(tem)
	ax1.plot(x, tem[x < 0.8], tem[x > 0.5],'bo',color='r')
	ax1.set_xlabel('time')
	ax1.set_ylabel('tem')
	ax1.set_title('temperatura en el tiempo')
	ax1.legend(['tem1','tem2'])
	ax2 = fig.add_subplot(221)


	plt.show()

leerTemperatura()


def escribirTemperatura():
	pass
