#version 3.11

#Dado un número entero, crea un algoritmo que determine si es par o impar.



def NumeroEntero(getInputUser):

        try:
            int(getInputUser)

            if getInputUser % 2==0:
                return f"El numero {getInputUser} es par"                
            else:
                return f"El numero {getInputUser} es impar"
                

        except ValueError:
            
                return "Ha habido un error."
                


if __name__=='__main__':
    NumeroEntero()
