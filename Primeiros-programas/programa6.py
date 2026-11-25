perguntas = ["Qual a capital do Brasil?", "Qual é a linguagem de programação que tem uma cobra como nome?", "Qual as cores da bandeira do Brasil?"]
respostas = ["Brasília", "Python", "Verde, Amarelo, Azul e Branco"]

acertos = 0 

for i in range(len(perguntas)):
    respostas_usuario = input(perguntas[i] + "")
    if respostas_usuario.strip().lower() == respostas[i].strip().lower():
        print("Voce acertou a resposta")
        acertos += 1
    else:
        print("Voce errou a resposta")

print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")