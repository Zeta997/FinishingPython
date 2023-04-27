import sys
# Crea un algoritmo que convierta grados Celsius a Fahrenheit


def celciusToFahrenheit(celcius=0.0):
    # Entrada
    celcius = celcius
    # Proceso
    fahrenheit = ((celcius*1.8)+32)
    # Salida
    return fahrenheit


if __name__ == "__main__":
    celcius = sys.argv[1]
    numero = float(celcius)
    print(f"{celcius}ºC to {celciusToFahrenheit(numero)}ºF")
