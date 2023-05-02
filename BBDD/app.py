#generar aleatoriamente una lista de 100 elementos 'H' y 'M'
#Llamar a una función llamada "ClasificarGenero" pasando la lista de personas como argumento. 
#La funcion clasifica y cuenta la cantidad
import random
import json
import MongoBD as mg
class Fichero():
    
    listaElementos=list()
    contenidoAnteriorLista=list()
    diccDatosJSON=dict()
    contador=0
    def main(self):
        while True:
            print('-------------Programa de Ficheros 1-------------')
            print('1-Crear lista aleatria')
            print('2-Recuperar lista')
            print('3-Mostrar la lista')
            print('4-Guardar la lista en fichero json')
            print('5- Servidor MongoDB')
            print('0-Salir')
            __inputUser=input('Seleccione una opcion: ')
            self.EleccionUsuario(__inputUser)
            if __inputUser=='0':
                break   

    def EleccionUsuario(self,parametro):
        if parametro=='1':
            self.GenerarListaGenero()
        elif parametro=='2':
            self.ComprobarFichero()
        elif parametro=='3':
            self.MostrarContenidoFicheroExistente()
        elif parametro=='4':
            self.CrearYGuardadFicheroJSON()
        elif parametro=='5':
            conexion=mg.FirstStepsMongoDB()
            conexion.main()
        elif parametro=='0':
            return
        else:
            print('Elija una opcion valida.')

    def ClasificarGenero(self):
        cantidadH=self.contenidoAnteriorLista.count('H')
        cantidadM=self.contenidoAnteriorLista.count('M')
        print(f'La cantidad de hombres es: {cantidadH}')
        print(f'La cantidad de mujeres es: {cantidadM}')
        print(f'El porcentaje de hombres es: {cantidadH:.2f}%')
        print(f'El porcentaje de mujeres es: {cantidadM:.2f}%')

    def GenerarListaGenero(self):
        print('Creando lista...')
        for x in range(1,101):
            generarGenero= random.randint(0,1)
            if generarGenero==0:
                self.listaElementos.append("H")
            else:
                self.listaElementos.append("M")
        print('Lista creada satisfactoriamente.')
        print('Creando fichero...')
        self.CreacionFichero()

    def CreacionFichero(self):
        __nombreFichero=input('Introduzca nombre para el fichero con su extension: ')
        tipoFichero=open(__nombreFichero, "wt", encoding='UTF-8')
        tipoFichero.write(f"{self.listaElementos}")
        print('Contenido del fichero escrito')
        tipoFichero.close()
        print('Fichero creado satisfactoriamente.')
    
    def ComprobarFichero(self):
        try:
            __nombreFichero=input('Introduzca el nombre del fichero que quiere recuperar junto con su extension: ')
            lecturaFichero=open(__nombreFichero,'rt', encoding='UTF-8')
            self.contenidoAnteriorLista=f'{lecturaFichero.read()}'
            lecturaFichero.close()
        except FileNotFoundError:
            print('Fichero no encontrado.')

    def CantidadHyM(self):
        cantidadH=self.contenidoAnteriorLista.count("H")
        cantidadM=self.contenidoAnteriorLista.count("M")
        self.diccDatosJSON["Elemento"]=self.contador
        self.diccDatosJSON["CantidadHombres"]=cantidadH
        self.diccDatosJSON["CantidadMujeres"]=cantidadM
        self.diccDatosJSON["PorcentajeHombres"]= cantidadH
        self.diccDatosJSON["PorcentajeMuejeres"]= cantidadM
        self.contador+=1
                
    def MostrarContenidoFicheroExistente(self):
        self.ClasificarGenero()
    
    def CrearYGuardadFicheroJSON(self):
        self.CantidadHyM()
        __inputUsuario=input('Introduce un nombre para el fichero json sin extension: ')
        try:
            crearficheroJSON=open(f"{__inputUsuario}.json",'x', encoding="UTF-8")
            contenido=self.diccDatosJSON
            ficheroJSON=json.dumps(contenido)                
            crearficheroJSON.write(ficheroJSON)     
            crearficheroJSON.close()
            print('Fichero JSON creado.')
        except FileExistsError:
            print(f'El fichero {__inputUsuario}.json existe.')
            


if __name__=='__main__':
    ejcute= Fichero()
    ejcute.main()
