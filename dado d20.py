
palavra = "mclaren"
letras_usuario = []
chances = 6
ganhou = False

while True:

    for letra in palavra:
        if letra.lower() in palavra_usuario:
            print(letra, end= "")
        else:

            print("_", end= "")
    print(f"Você tem {chances} chances")           
    tentativa = input("Escolha uma letra para adivinhar: ")
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in palavras_usuario:
            ganhou = False


    if chances == 0or ganhou:
        break



if ganhou:
    print(f"ganhou. A palavra era: {palavra}")
else:
    print(f"Ai não irmão, ai tu tá errado! A palavra era: {palavra}")
