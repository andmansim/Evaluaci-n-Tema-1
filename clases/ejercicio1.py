

def limpiar(matriz):
    
 
    for i in range(len(matriz)): 
        suma = 0
        for j in range(len(matriz)):
        
            if j < 3:
                suma = matriz[i][j] + suma
                
            elif j == 3:
                if suma == matriz[i][-1]:
                    pass
                else:
                    matriz[i][-1] = suma
                    
        
limpiar(matriz)
print(matriz)