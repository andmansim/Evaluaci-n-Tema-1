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
