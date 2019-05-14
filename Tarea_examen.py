class sumas (object):
    def __init__(self):
        pass
    def matriz(self, matriz):
        if isinstance (matriz, list):
            return self.matrices(matriz, 0, 0, 'a',())
        else:
            return 'Error'

    def matrices(self, matriz, fila, columna, parada, resultado):
        if parada == 0:
            return resultado
        elif parada == 'a':
            return self.matrices(matriz, fila, columna, 'b', resultado + self.a(matriz, 0, 0, 'a', 0))
        elif parada == 'b':
            return self.matrices(matriz, fila, columna, 'c', resultado + self.b(matriz, 0, 0, 'b', 0))
        elif parada == 'c':
            return self.matrices(matriz, fila, columna, 'd', resultado + self.c(matriz, 0, len(matriz[0])-1, 'c', 0))
        else:
            return self.matrices(matriz, fila, columna, 0, resultado + (resultado[0] + resultado[1] + resultado[2],))




    def a (self, matriz, fila, columna, parada, resultado):
        if fila > len(matriz):
            return (resultado,)
        elif parada == 'a':
            if columna == len(matriz[0]):
                return self.a(matriz, (fila + len(matriz))-1, 0, 'a', resultado)
            else:
                return self.a(matriz, fila, columna + 1, parada, resultado + matriz[fila][columna]) 

    def b (self, matriz, fila, columna, parada, resultado):
        if fila == len(matriz):
            return (resultado,)
        elif parada == 'b':
            if columna > len(matriz[0])-1:
                return self.b(matriz, fila + 1, 0, 'b', resultado)
            else:
                return self.b(matriz, fila, columna + len(matriz[0])-1, parada, resultado + matriz[fila][columna])

    def c (self, matriz, fila, columna, parada, resultado):
        if fila == len(matriz):
            return (resultado,)
        elif parada == 'c':
            if columna < 0:
                return self.c(matriz, fila + 1, 0, 'c', resultado)
            else:
                return self.c(matriz, fila + 1, columna - 1, parada, resultado + matriz[fila][columna])

    
#______________________________________________________________________________________________________________________________________________________________________
class matriz(object):
    
    def __init__(self):
        pass
    def matriz_1(self, matriz):
        if isinstance (matriz,list):
            return self.calcular(matriz, ())
        else:
            return 'Error'

    def calcular(self, matriz, resultado):
        if len(resultado) == 2:
            return resultado
        elif len(resultado) == 0:
            return self.calcular(matriz, resultado + self.promedio(matriz, 0, 0))
        elif (len(matriz) * len(matriz[0])) % 2 == 1:
            return self.calcular(matriz, resultado + self.mediana(matriz, len(matriz)/2 - 0.5, len(matriz[0])/2 - 0.5  ,False, 0))
        else:
            return self.calcular(matriz, resultado + self.mediana_2(matriz, (len(matriz)/2)-1, len(matriz[0]) - 1  ,False, 0))

    def promedio(self, matriz, indice, resultado):
    
        if indice == len(matriz):
            return (int(resultado),)
        else:
            return self.promedio(matriz, indice + 1, (resultado + (matriz[indice][indice]/len(matriz))))

    def mediana(self, matriz, fila, columna, parada, resultado):

        if parada == True:
            return (int(resultado),)
        else:
            return self.mediana(matriz, fila, columna, True, resultado + (matriz[int(fila)][int(columna)]/2))

    def mediana_2(self, matriz, fila, columna, parada, resultado):
       
        if parada == True:
            return (int(resultado),)
        else:
            return self.mediana(matriz, fila, columna, True, resultado + ((matriz[int(fila)][int(columna)]) + (matriz[int(fila + 1)][0]))/2)  

#_____________________________________________________________________________________________________________________________________________________________________

class polinomio(object):
    
    def __init__(self):
        pass
    def polinomio_1(self, num1, num2):
        if isinstance (num1, int) and (num2, int):
            return self.calcular(num1, num2, num1 - 1, 1)
        else:
            return 'Error'

    def calcular(self, num1, num2, r, s):
        if num1 == r+s and num2 == r*s:
            return (r,s)
        else:
            return self.calcular(num1, num2, r-1, s+1)

#_____________________________________________________________________________________________________________________________________________________________________
class Cientifica(object):
	def _init_(self):
		pass

	def notacion(self,numero):
		if numero != 0:
			return self.conversion(numero,0)
		else:
			return "Error el numero no puede ser 0"

	def conversion(self,numero,exponente):
		if 1 <= numero < 10:
	 		return str(numero) +" x 10 ** "+str(exponente)
		elif numero < 1:
			return self.conversion(numero*10,exponente-1)
		else:
			return self.conversion(numero//10,exponente+1)









            
