def media(media):
    if media > 6:
        return "Aprovado"
    elif 4 <= media <= 6:
        return "Verificação Suplementar"
    else:
        return "Reprovado"

def main():
    try:
        media_aluno = float(input("Digite a média do aluno: "))
        status = media(media_aluno)
        print(f"Status do aluno: {status}")
    except ValueError:
        print("Erro: Por favor, insira uma média válida.")

if __name__ == "__main__":
    main()