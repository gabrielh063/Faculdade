def obter_melhor_volta(matriz_tempos):
    melhor_volta = float('inf')
    piloto_melhor_volta = ""
    volta_melhor_volta = 0

    for i in range(len(matriz_tempos)):
        for j in range(len(matriz_tempos[i])):
            if matriz_tempos[i][j] < melhor_volta:
                melhor_volta = matriz_tempos[i][j]
                piloto_melhor_volta = f"Corredor {i + 1}"
                volta_melhor_volta = j + 1

    return piloto_melhor_volta, volta_melhor_volta


def obter_classificacao_final(matriz_tempos):
    tempos_finais = [sum(corredor) for corredor in matriz_tempos]
    classificacao = sorted(range(len(tempos_finais)), key=lambda k: tempos_finais[k])
    return [f"Corredor {i + 1}" for i in reversed(classificacao)]


def obter_volta_media_rapida(matriz_tempos):
    medias_por_volta = [sum([corredor[i] for corredor in matriz_tempos]) / len(matriz_tempos) for i in range(len(matriz_tempos[0]))]
    volta_media_rapida = medias_por_volta.index(min(medias_por_volta)) + 1
    return volta_media_rapida
num_corredores = 6
num_voltas = 10

matriz_tempos = []
for i in range(num_corredores):
    tempos = []
    print(f"Insira os tempos das {num_voltas} voltas para o Corredor {i + 1}:")
    for j in range(num_voltas):
        tempo = float(input(f"Volta {j + 1}: "))
        tempos.append(tempo)
    matriz_tempos.append(tempos)
melhor_volta, volta_melhor_volta = obter_melhor_volta(matriz_tempos)
print(f"\nMelhor volta da prova: {melhor_volta}, na volta {volta_melhor_volta}")
classificacao_final = obter_classificacao_final(matriz_tempos)
print("\nClassificação final:")
for i, corredor in enumerate(classificacao_final):
    print(f"{i + 1}º lugar: {corredor}")
volta_media_rapida = obter_volta_media_rapida(matriz_tempos)
print(f"\nVolta com a média mais rápida: Volta {volta_media_rapida}")
