def imprimir_matriz(matriz):
    for linha in matriz:
        print("|", end=" ")
        for elemento in linha:
            print(elemento, end=" ")
        print("|")
def multiplicar_diagonal_principal(matriz, k):
    for i in range(len(matriz)):
        matriz[i] *= k
matriz_3x3 = []
for _ in range(3):
    linha = [int(x) for x in input("Digite os elementos da linha separados por espaço: ").split()]
    matriz_3x3.append(linha)
print("Matriz antes da multiplicação:")
imprimir_matriz(matriz_3x3)
k = int(input("Digite o valor de k: "))
multiplicar_diagonal_principal(matriz_3x3, k)
print("\nMatriz após a multiplicação:")
imprimir_matriz(matriz_3x3)
