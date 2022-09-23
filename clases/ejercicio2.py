class Cadena:
    def __init__(self, usuario):
        self.usuario = usuario
        

        
    def comprobar(self):
        if  len(self.usuario) == 3 or  3 < len(self.usuario) < 10:
            return True
        else:
            return False