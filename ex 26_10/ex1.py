import math

def combinacao(N, M):
    combinacoes = math.factorial(N) / (math.factorial(M) * math.factorial(N - M))
    return combinacoes

def main():
    N = int(input("Digite o número total de alunos (N): "))
    M = int(input("Digite o número de alunos no primeiro grupo (M): "))

    if M < 0 or M > N:
        print("Erro: M deve estar entre 0 e N.")
        return

    resultado = combinacao(N, M)
    print(f"O número de combinações possíveis é: {resultado}")

if __name__ == "__main__":
    main()