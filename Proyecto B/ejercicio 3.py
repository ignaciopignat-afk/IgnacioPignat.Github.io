input("ingrese su nombre de usuario")

for i in range(1,6):

    vidas= int(input("ingrese la cantidad de vidas que desee para su personaje:"))

    if vidas >= 5:
        print("el juego esta en nivel facil")

    if vidas <= 4 and vidas >= 3:
        print("el juego esta en nivel medio")

    if vidas <= 2 and vidas >= 1:
        print("el juego esta en nivel dificil")
