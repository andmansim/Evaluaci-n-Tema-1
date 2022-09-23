from clases.ejercicio2 import *
from clases.ejercicio1 import*

if __name__=='__main__':
    print('Qué ejercicio quieres ejecutar?')
    #Ejercicio 2
    u = input()
    if u == 2:
        c = Cadena()
        print('Introduzca una frase')
        usuario = str(input())
        c.usuario(usuario)
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
    