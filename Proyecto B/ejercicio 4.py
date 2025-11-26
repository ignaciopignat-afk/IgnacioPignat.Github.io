
import random


def jugar_dados(tiradas):
    total = 0
    for i in range(tiradas):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        print(f"Tirada {i+1}: dado1 = {dado1}, dado2 = {dado2}, suma = {suma}")
        total += suma
    return total


tiradas = int(input("Ingrese la cantidad de tiradas por jugador: "))

print("\nJugador 1")
total_jugador1 = jugar_dados(tiradas)
print(f"Total jugador 1: {total_jugador1}\n")

print("Jugador 2")
total_jugador2 = jugar_dados(tiradas)
print(f"Total jugador 2: {total_jugador2}\n")

# Determinar el ganador
if total_jugador1 > total_jugador2:
    print("Gana el Jugador 1")
elif total_jugador2 > total_jugador1:
    print("Gana el Jugador 2")
else:
    print("¡Es un empate!")