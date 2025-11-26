def mostrar_tabuleiro(tab):
    for linha in tab:
        print(" | ".join(linha))


def verificar_vitoria(tab, jogador):
    for i in range(3):
        if (
            tab[i][0] == jogador
            and tab[i][1] == jogador
            and tab[i][2] == jogador
        ):
            return True

    for i in range(3):
        if (
            tab[0][i] == jogador
            and tab[1][i] == jogador
            and tab[2][i] == jogador
        ):
            return True

    if tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador:
        return True

    if tab[0][2] == jogador and tab[1][1] == jogador and tab[2][0] == jogador:
        return True

    return False


tabuleiro = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

while True:
    escolha_inicial = input("Jogador inicial vai ser X ou O: ")

    if escolha_inicial.upper() == "X":
        jogador_atual = "X"
        break
    elif escolha_inicial.upper() == "O":
        jogador_atual = "O"
        break
    else:
        print("Valor ilegivel")

for rodada in range(9):
    mostrar_tabuleiro(tabuleiro)

    escolha = input(f"Jogador {jogador_atual}: ")
    pos = int(escolha) - 1
    linha, coluna = pos // 3, pos % 3

    if tabuleiro[linha][coluna] in ["X", "O"]:
        print("Posição ja ocupada")
        continue

    tabuleiro[linha][coluna] = jogador_atual

    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual} ganhou!")
        break

    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"
else:
    mostrar_tabuleiro(tabuleiro)
    print("Empate!")
