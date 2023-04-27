# hasta que el usuario adivine el número correcto.
import random
import sys


def aleatorio():
    return random.randint(1, 100)


def adivinaNumero(ramdon, numero):
    ramdon = int(ramdon)
    numero = int(numero)
    if (numero == ramdon):
        return f"Has adivinado el numero era {ramdon}"
    elif (numero > ramdon):
        return f"Has introducido un numero mayor que el aleatorio"
    elif (numero < ramdon):
        return f"Has introducido un numero menor que el aleatorio"
