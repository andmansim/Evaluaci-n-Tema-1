class Cadena:
    def __init__(self):
        self.__usuario = 0
        
    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, nuevo):
        self.__usuario = nuevo
        
    def comprobar(self):
        if  len(self.__usuario) == 3 or  3 < len(self.__usuario) < 10:
            return True
        else:
            return False