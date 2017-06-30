import numpy as np

a = np.zeros((5,2))

for x in range(0,4):
	print('---')
	a[x,1] = np.random.rand(1)

print(a)
def leer():
	f = open('file.txt','r', encoding='utf-8')
	contenido = f.read()
	print(contenido)
	f.close()

def escribir():
	lista = ('Lunes','Martes','Miercoles','Jueves','Viernes')
	archivo = open('file.txt','w')
	archivo.writelines(lista)
	archivo.close


escribir()
leer()