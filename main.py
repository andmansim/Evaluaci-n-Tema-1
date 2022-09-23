from clases.ejercicio2 import *

if __name__=='__main__':
    c = Cadena()
    print('Introduzca una frase')
    usuario = str(input())
    c.usuario(usuario)
    print(c.usuario)
    prueba = c.comprobar()
    print(prueba)