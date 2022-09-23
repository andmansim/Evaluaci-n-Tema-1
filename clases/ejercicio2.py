class Cadena:
    def __init__(self):
        self.__usuario = 0
        
    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, nuevo):
        self.__usuario = nuevo
        

