matriz_pessoas = []
for _ in range(10):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade de {}:".format(nome)))
    matriz_pessoas.append([nome, idade])
pessoa_mais_nova = min(matriz_pessoas, key=lambda x: x[1])
print("A pessoa mais nova é:", pessoa_mais_nova[0])
