# Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista.
import sys


def stringToList(numeros=""):
    listaNumeros = numeros.split(",")
    return listaNumeros


def listStrToFloat(lista=[]):
    listaFloat = [float(i) for i in lista]
    return listaFloat


def mediaAritmetica(lista=[]):
    suma = sum(lista)
    return suma/len(lista)


if __name__ == "__main__":
    lista = sys.argv[1]
    numeros = listStrToFloat(stringToList(lista))
    print(f"La media aritmetica es {mediaAritmetica(numeros)}")
