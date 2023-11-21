def somar(memoria, numero):
    return memoria + numero

def subtrair(memoria, numero):
    return memoria - numero

def multiplicar(memoria, numero):
    return memoria * numero

def dividir(memoria, numero):
    if numero != 0:
        return memoria / numero
    else:
        print("Nao é possivel dividir por zero")
        return memoria

def limpar_memoria():
    return 0

def main():
    memoria = 0

    while True:
        print(f"Estado da memória: {memoria}")
        print("Opções:")
        print("(1) Somar")
        print("(2) Subtrair")
        print("(3) Multiplicar")
        print("(4) Dividir")
        print("(5) Limpar memória")
        print("(6) Sair do programa")

        opcao = input("Qual opção você deseja? ")

        if opcao == '1':
            numero = float(input("Digite o número para somar: "))
            memoria = somar(memoria, numero)
        elif opcao == '2':
            numero = float(input("Digite o número para subtrair: "))
            memoria = subtrair(memoria, numero)
        elif opcao == '3':
            numero = float(input("Digite o número para multiplicar: "))
            memoria = multiplicar(memoria, numero)
        elif opcao == '4':
            numero = float(input("Digite o número para dividir: "))
            memoria = dividir(memoria, numero)
        elif opcao == '5':
            memoria = limpar_memoria()
        elif opcao == '6':
            print("Saindo.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()