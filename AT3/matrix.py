def transpor_matriz(matriz):
    """Transforma linhas de uma matriz $M \times N$ em colunas ($N \times M$)."""
    # Usando list comprehension para criar a transposta
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def multiplicar_matriz(matriz_a, matriz_b):
    """Realiza a multiplicação matricial clássica: Linha por Coluna."""
    # Validação: Colunas de A devem ser iguais às Linhas de B
    if len(matriz_a[0]) != len(matriz_b):
        print("Erro: O número de colunas de A deve ser igual ao número de linhas de B.")
        return None
    
    # Cria matriz resultante preenchida com zeros
    resultante = [[0 for _ in range(len(matriz_b[0]))] for _ in range(len(matriz_a))]
    
    # Algoritmo de multiplicação
    for i in range(len(matriz_a)):
        for j in range(len(matriz_b[0])):
            for k in range(len(matriz_b)):
                resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]
                
    return resultante