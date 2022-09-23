# Evaluaci-n-Tema-1
 Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/Evaluaci-n-Tema-1.git)
 https://github.com/andmansim/Evaluaci-n-Tema-1.git
He realizado una serie de ejercicios, los cuales son:
# Main
'''
from clases.ejercicio2 import *
from clases.ejercicio1 import*
from clases.ejercicio3 import*
from clases.tabla import*

if __name__=='__main__':
    print('Qué ejercicio quieres ejecutar?')
    #Ejercicio 2
    u = input()
    if u == 2:
        
        print('Introduzca una frase')
        usuario = str(input())
        c = Cadena(usuario)
        prueba = c.comprobar()
        print(prueba)
    elif u == 1:
        #Ejercicio 1
        matriz = [[1,1,1,3],
          [2, 2, 2, 7], 
          [3, 3, 3, 9], 
          [4, 4, 4, 13]]
        limpiar(matriz)
        print(matriz)
    elif u == 3:

        lista1 = generar_listas(0, 10, 1)
        print(lista1)
        lista2 = generar_listas(-10, 0, 1)
        print(lista2)
        lista3 = generar_listas(0, 20, 2)
        print(lista3)
        lista4 = generar_listas(-20, 0, 2)
        print(lista4)
        lista5 = generar_listas(0, 50, 5)
        print(lista5)
    elif u == 4:
        #Ejercicio 4
        print('Introduce dos números del 0 al 9')
        print('Número 1')
        n1 = input()
        print('Número 2')
        n2 = input()
        t = Tabla(n1, n2)
        tabla = t.construir_tabla()
        print(tabla)

 '''
 # Ejercicio 1
 
 '''
 def limpiar(matriz):
    
 
    for i in range(len(matriz)): 
        suma = 0
        for j in range(len(matriz)):
        
            if j < 3:
                suma = matriz[i][j] + suma
                
            elif j == 3:
                if suma == matriz[i][-1]:
                    pass
                else:
                    matriz[i][-1] = suma
                    
        
 '''
 # Ejercicio 2
 '''
 class Cadena:
    def __init__(self, usuario):
        self.usuario = usuario
        

        
    def comprobar(self):
        if  len(self.usuario) == 3 or  3 < len(self.usuario) < 10:
            return True
        else:
            return False
 '''
# Ejercicio 3
'''

def generar_listas(inicio, fin, salto):
    lista = []
    for i in range(inicio, fin + 1, salto):
        lista.append(i)
    return lista

'''

# Ejercicio 4
'''

class NumIncorrecto(BaseException):
    pass

class Tabla:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def errores(self):
        try:
            self.n1.isnumeric()
            
        except NumIncorrecto:
            print('Debe de ser un número del 0 al 9')
            n1 = input()
            Tabla(n1, self.n2)
        try:
            self.n2.isnumeric()
            
        except NumIncorrecto:
            print('Debe de ser un número del 0 al 9')
            n2 = input()
            Tabla(self.n1, n2)
    
    def construir_tabla(self):
        filas = [''] * self.n1
        lista = ','.join(filas)
        columnas = (lista + '\n ') * self.n2
        lista1 = ','.join(columnas)
        lista2 = [lista1]
        return lista2
'''
