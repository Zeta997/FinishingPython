#version 3.11

#Crea un algoritmo que calcule el factorial de un número entero.
import math

def Factorial(getInputUser):

        try: 
            int(getInputUser)
            _factorial = math.factorial(getInputUser)
            return f"El factorial de {getInputUser} es {_factorial}"
        except ValueError:
            return "Solo se permiten valores enteros."
            

if __name__=='__main__':
    Factorial()