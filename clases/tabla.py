
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
            
        
            
           