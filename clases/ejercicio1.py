
matriz = [[1,1,1,3],
          [2, 2, 2, 7], 
          [3, 3, 3, 9], 
          [4, 4, 4, 13]]

def limpiar(matriz):
    suma = 0
    j = 0
 
    for i in range(len(matriz)): 
    
        for j in range(len(matriz)):
        
            if j < 3:
                suma = matriz[i][j] + suma
                print(suma)
        
limpiar(matriz)
