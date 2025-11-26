import random

tiradas = int(input("ingrese la cantidad de tiradas: "))

contador=0
total=0

while contador < tiradas:
    dado1= random.randint(1,6)
    dado2= random.randint(1,6)
    suma= dado1 + dado2
    print(f"tirada", contador + 1,": dado 1=",dado1," y dado 2=", dado2," suma=",suma)
    total += suma
    contador += 1
print("la suma total de todas las tiradas es: ",total)
