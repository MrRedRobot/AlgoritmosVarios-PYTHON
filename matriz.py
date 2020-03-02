def crearLista(N):
    L = [ ]
    for i in range(N):
        L.append(random.randint(0,100))
    return L
 
def CreaMatriz(N,M):
    Matriz = [ ]
    for i in range(N):
        Matriz.append(crearLista(M))
    for i in range(N):
        Fila = ""
        for j in range(M):
            Espacios = ' ' * (5-len(str(Matriz[i][j])))
            Fila = Fila + Espacios + str(Matriz[i][j])
        print (Fila)
    return Matriz
