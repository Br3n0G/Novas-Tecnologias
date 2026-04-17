from matrix import transpor_matriz, multiplicar_matriz

# --- Exemplo 1: Transposição ---
print("Exemplo de Transposição:")
A = [[1, 2], [3, 4], [5, 6]]
print(f"Original: {A}")
print(f"Transposta: {transpor_matriz(A)}")

print("\n" + "-"*30 + "\n")

# --- Exemplo 2: Multiplicação ---
print("Exemplo de Multiplicação:")
matriz_1 = [[1, 2], [3, 4]]
matriz_2 = [[5, 6], [7, 8]]

resultado = multiplicar_matriz(matriz_1, matriz_2)
print(f"A: {matriz_1}")
print(f"B: {matriz_2}")
print(f"A * B = {resultado}")