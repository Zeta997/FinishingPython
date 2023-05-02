#version 3.11

#Calcula el área y perímetro de un círculo dado su radio.

import math

_pi=math.pi



def Area(area):
    
        int(area)
        
        _calculoA= _pi*pow(area,2)
        return f"El área del circulo es: {round(_calculoA,2)}"          



def Perimetro(perimetro):

        int(perimetro)
        _calculoP= 2*_pi*perimetro
        return f"El Perimetro es: {round(_calculoP,2)}"
    


if __name__=='__main__':
    Area()
    Perimetro()