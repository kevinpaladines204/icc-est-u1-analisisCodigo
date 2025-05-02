#Archivo principal
#import benchmarking as bm
#from benchmarking import Benchmarking
import benchmarking as bm
from metodos_ordenamiento import MetodosOrdenamiento

if __name__=="__main__":
    print("Funciona")
    #bm.Benchmarking()
    #Benchmarking()
    
    bench = bm.Benchmarking()
    metodosO= MetodosOrdenamiento()
    
    ##tam = 10000
    tamanios=[5000,10000, 10500]
    resultados= []
    
    for tam in tamanios:
    
        arreglo_base = bench.build_arreglo(tam)
        metodos_dicc={
            "burbuja":metodosO.sort_Bubble,
            "burbuja mejorado":metodosO.sort_burbuja_mejorado_optimizado,
            "seleccion":metodosO.sort_seleccion,
            "shell": metodosO.sort_shell
        }
    
        for nombre,fun_metodo in metodos_dicc.items():
            tiempo_resultado= bench.medir_tiempo(fun_metodo,arreglo_base)
            tupla_resultado=(tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)
    
    for tam, nombre, tiempo_resultado in resultados:
        print(f'tamano : {tam}, nombre metodo : {nombre}, tiempo : {tiempo_resultado:.6f} segundos')