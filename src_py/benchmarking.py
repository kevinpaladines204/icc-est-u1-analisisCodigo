from metodos_ordenamiento import MetodosOrdenamiento
import random
import time

class Benchmarking:


    def __init__(self):
        print ('Benchmarking instanciado')
        
    def medir_tiempo(self, funcion, arreglo):
        inicio= time.perf_counter()
        funcion(arreglo)
        fin=time.perf_counter()
        return fin-inicio
        
        
        
        
        
        
        
        
        
        
        
        """
        self.mO= MetodosOrdenamiento()

        arreglo= self.build_arreglo(10000)

        tarea=lambda: self.mO.sort_Bubble(arreglo)

        tiempo_milisegundos = self.contar_con_current_time_milles(tarea)
        print(f"Tiempo en milisegundos: {tiempo_milisegundos * 1000:.2f} ")

        tiempo_nanosegundos = self.contar_con_nano(tarea)
        print(f"Tiempo en nanosegundos: {tiempo_nanosegundos:.2f} ")


        tiempo_bubble = self.contar_con_nano(lambda: self.mO.sort_Bubble(arreglo.copy()))
        print(f"Tiempo en Nanosegundos con Met.Bubble Sort: {tiempo_bubble} ")

        tiempo_burbuja_mejorado = self.contar_con_nano(lambda: self.mO.sort_burbuja_mejorado_optimizado(arreglo.copy()))
        print(f"Tiempo en Nanosegundos con Met.Burbuja Mejorado: {tiempo_burbuja_mejorado}")

        tiempo_seleccion = self.contar_con_nano(lambda: self.mO.sort_seleccion(arreglo.copy())) 
        print(f"Tiempo de Nanosegundos con Met.Selección: {tiempo_seleccion} ")
        
        tiempo_shell= self.contar_con_nano(lambda: self.mO.sort_shell(arreglo.copy()))
        print(f"Tiempo de Nanosegundos con Met.Shell: {tiempo_shell} ")

        """
        
    def build_arreglo(self, tamano):
        arreglo= []
        for _ in range (tamano):
            numero=random.randint(0,99999)
            arreglo.append(numero)
        return arreglo

    def contar_con_current_time_milles(self, tarea):
        inicio= time.time()
        tarea()
        fin= time.time()
        return(fin - inicio)
        

    def contar_con_nano(self, tarea):
        inicio= time.time_ns()
        tarea()
        fin= time.time_ns()
        return(fin-inicio)/1_000_000_000
    


