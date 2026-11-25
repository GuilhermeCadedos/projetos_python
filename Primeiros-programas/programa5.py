pergunta = input("Qual linguagem está ligada a estilização de páginas web? ")

match pergunta.strip().upper():
    case "CSS":
        print("Você acertou a linguagem")
    case "HTML": 
        print("Você errou a linguagem")
    case "JavaScript":
        print("Você errou a linguagem")
    case _:
        print("Você errou a linguagem")