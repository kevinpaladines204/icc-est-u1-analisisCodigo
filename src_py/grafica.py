import matplotlib.pyplot as plt

#creacion de un grafico de lineas
x = [1,2,3,4,5]
y = [2,4,6,8,10]
 
 
plt.plot(x,y, label="linea", color ="green")

#agregar parametros
plt.title("Mi primer grafico en python")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")


#agregar leyenda
plt.legend()


#mostrar ventana de grafico
plt.show()