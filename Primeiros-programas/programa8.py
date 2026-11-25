tabuleiro =[ ["","",""],
             ["","",""],
             ["","",""]]
tabuleiro[2][2] = "💎"

tentativas = 0

def mostrar_tabuleiro():
    for linha in tabuleiro:
        print("|".join(linha))
        print("-"*5)

def tesouro_encontrado(linha,coluna):
    if tabuleiro[linha][coluna] == "💎":
        print("Jogador encontrou o tesouro!")
    elif tabuleiro[linha][coluna] == "X":
        print("Jogador já tentou essa posição!!")
    else:
        print("Jogador errou!")
        tabuleiro[linha][coluna] = "X"


while tentativas < 5:
    coluna = int(input("Digite a coluna: "))
    linha = int(input("Digite a linha: "))
    tentativas += 1


    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
      print("Essa posição é invalida!")
    elif tabuleiro[linha][coluna] == "💎":
        print("Você encontrou o tesouro")
        
        break
    else:
        tesouro_encontrado(linha, coluna)
        mostrar_tabuleiro()



