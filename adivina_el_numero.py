# se le pedira al usuario que trate de adivinar un numero entre el 1 y el 50
# el usuario tendra una cantidad limitada de intentos la cual sera de 5  para adivinar el numero
# si el usuario supera el limite de intentos tendra que volver a empezar

import random

intentos = 5
numero_aleatorio = random.randint(1, 50)
while True:
	adivina_num = int(input("\nhola usuario intente adivinar un numero entre el 1 y el 50 tienes 5 intentos: "))
	if intentos == 0:
		print("\ncasi lo logras pero tal parece quer te quedaste sin intentos")
		revelacion = str(input("te gustaria ver que numero era?: "))
		if revelacion.lower() == "si":
			print(f"lastima, casi lo lograste el numero era {numero_aleatorio}")
			break

		elif revelacion.lower() == "no":
			print("bueno si tu lo dices amigo/a, deberias intentarlo otra vez :D")
			break

	if (adivina_num < 1) or (adivina_num > 50):
                intentos -= 1
                print("\nno te salgas de los limites, por gracioso pierdes un intento")
                print(f"te quedan {intentos} intentos")

	elif adivina_num == numero_aleatorio:
		print("!felicidades lo haz logrado adivinar, que habilidoso¡")
		break

	elif adivina_num < numero_aleatorio:
		intentos -= 1
		print("\ncasi lo logras pero el numero es de mayor valor")
		print(f"te quedan {intentos} intentos")

	elif adivina_num > numero_aleatorio:
		intentos -= 1
		print("\ncasi lo logras pero el numero es de menor valor")
		print(f"te quedan {intentos} intentos")




