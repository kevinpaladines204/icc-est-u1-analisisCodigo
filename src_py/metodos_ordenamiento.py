
class MetodosOrdenamiento:
    def sort_Bubble(self, array):
        arreglo=array.copy()
        print("metodo")
        n= len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i]> arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo
    

    #programar cada metodo
    #medir tiempo con nano
    #imprimir 3 resultados indicando cual es el mas optimo

    def sort_burbuja_mejorado_optimizado(self,array):
        arreglo=array.copy()
        n= len(arreglo)
        intercambio= True
        for i in range(n):
            if not intercambio:
                break
            intercambio=False
        
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                intercambio = True 
        return arreglo

        

    def sort_seleccion(self, array):
        arreglo=array.copy()
        n = len(arreglo)
        for i in range(n):
            indice_minimo=i
            for j in range(i+1,n):
                if arreglo[j]>arreglo[indice_minimo]:
                    indice_minimo=j
                    arreglo[i],arreglo[indice_minimo]= arreglo[indice_minimo], arreglo[i]
        return arreglo
