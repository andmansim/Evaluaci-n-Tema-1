
matriz = [[1,1,1,3],
          [2, 2, 2, 7], 
          [3, 3, 3, 9], 
          [4, 4, 4, 13]]

def limpiar():
    for i in matriz:
        for j in matriz:
            if sum(matriz[i][:-1]) == matriz[i][-1]:
                pass
            else:
                matriz[i][-1] = sum(matriz[i][:-1])
