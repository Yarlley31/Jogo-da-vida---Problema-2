# função para criar uma matriz 10x10 preenchida com ' '
def criar_matriz_10x10():
    matriz10x10 = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(' ')  
        matriz10x10.append(linha)
    return matriz10x10
