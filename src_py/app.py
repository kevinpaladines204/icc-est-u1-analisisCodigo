#Archivo principal
#import benchmarking as bm
#from benchmarking import Benchmarking
import benchmarking as bm
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
import datetime

if __name__=="__main__":
    print("Funciona")
    #bm.Benchmarking()
    #Benchmarking()
    
    bench = bm.Benchmarking()
    metodosO= MetodosOrdenamiento()

    tamanios=[500,1000,2000]
    resultados= []
    
    for tam in tamanios:
    
        arreglo_base = bench.build_arreglo(tam)
        metodos_dicc={
            "burbuja":metodosO.sort_Bubble,
            "burbuja mejorado":metodosO.sort_burbuja_mejorado_optimizado,
            "seleccion":metodosO.sort_seleccion,
            "shell": metodosO.sort_shell,
            "inserccion": metodosO.sort_inserccion
        }
    
        for nombre,fun_metodo in metodos_dicc.items():
            tiempo_resultado= bench.medir_tiempo(fun_metodo,arreglo_base)
            tupla_resultado=(tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)
    
    for tam, nombre, tiempo_resultado in resultados:
        print(f'tamano : {tam}, nombre metodo : {nombre}, tiempo : {tiempo_resultado:.6f} segundos')
        
    #preparar datos para ser graficados
    #crear diccionario o map para almacenar resultados por metodos 
    
    #fecha y hora
    fecha_hora_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    titulo_general = f"Kevin Paladines - {fecha_hora_actual}"

    tiempos_by_metodos={
        "burbuja": [],
        "burbuja mejorado": [],
        "seleccion": [],
        "shell": [],
        "inserccion": []
    }
    
    for tam,nombre,tiempo in resultados:
        tiempos_by_metodos[nombre].append(tiempo)

    plt.figure(figsize=(10,6))
    plt.subplot(1,2,1)
    
    #graficar los tiempos de ejecucion
    for nombre,tiempos in tiempos_by_metodos.items():
        plt.plot(tamanios,tiempos, label=nombre, marker="o")
        
    #agregar parametros de grafico
    plt.title("Comparativa de tiempos para cada metodo de ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo de ejecucion (s)")
    
    plt.legend()
    
    
    #grafico 2
    plt.subplot(1,2,2)
    x = [1,2,3,4,5]
    y = [2,4,6,8,10]
 
 
plt.plot(x,y, label="linea", color ="green")
plt.title("Mi primer grafico en python")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()


plt.suptitle(titulo_general, fontsize=14, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
