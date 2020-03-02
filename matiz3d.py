
d=0
matriz3d= []
matriz2d=[[0 for x in range(10)] for y in range(10)]
matriz=[]

for k in range (10):
    
    matriz3d.append(matriz2d)

    for i in range (10):
        
        matriz2d.append(matriz)
        matriz.append([])
        
        for j in range (10):
            for n in range (10):
                matriz[i].append(d)
                d += 1

print(matriz)
