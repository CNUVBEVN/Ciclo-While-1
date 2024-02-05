import random

def juego_adivinanza():
    # Paso 1: Generar un número aleatorio
    numero_secreto = random.randint(1, 100)

    # Paso 2: Inicializar la variable de intentos
    intentos = 0

    # Paso 3: Mostrar un mensaje de bienvenida
    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        # Paso 4: Incrementar la variable de intentos
        intentos += 1

        # Pedir al usuario que ingrese un número
        intento_usuario = int(input("Ingresa tu suposición: "))

        # Comprobar si el número es igual al numero_secreto
        if intento_usuario == numero_secreto:
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
            break
        elif intento_usuario > numero_secreto:
            print("Demasiado alto. Intenta nuevamente.")
        else:
            print("Demasiado bajo. Intenta nuevamente.")

    # Paso 5: Mostrar un mensaje de despedida y el número secreto
    print(f"¡Gracias por jugar! El número secreto era: {numero_secreto}")

if __name__ == "__main__":
    juego_adivinanza()
