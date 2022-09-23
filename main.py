from clases.ejercicio2 import *

if __name__=='__main__':
    c = Cadena()
    print('Introduzca una frase')
    usuario = input()
    c.usuario(usuario)
    prueba = c.comprobar()
    print(prueba)