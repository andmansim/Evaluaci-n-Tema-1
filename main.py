from clases.ejercicio2 import *
from clases.ejercicio1 import*
from clases.ejercicio3 import*

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
        
