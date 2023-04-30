#importacion de librerias

from pymongo.mongo_client import MongoClient
import json
class FirstStepsMongoDB():
    
    def main(self):
            
            while True:
                print('-------------Conexion al Servidor MongoDB-------------')
                print('1.-Conectar a la base de datos')
                print('2.-Subir fichero JSON.')
                print('3.-Mostrar fichero.')
                print('4.-Eliminar un elemento de la base de datos.')
                print('5.-Actualizar o agregar un dato de la base de datos.')
                print('0.-Salir')
                inputUser=input('Elije una opcion: ')
                self.OpcionElejida(inputUser)
                if inputUser=='0': 
                    break
                        

    def OpcionElejida(self,parametro):
            
            if parametro=='1':
                try:
                
                    #conectamos con el servidor una vez inicializado
                    self.test_client= MongoClient('mongodb://127.0.0.1:27017/')
                    print('Conexion exitosa.')  
                    self.db=self.test_client.admin

                    #Asignacion de nombres para la base de datos y la coleccion
                    self.db_name=self.test_client["GeneroPersonas"]
                    self.col_name=self.db_name['HombresyMujeres']

                    #obtenemos los parametros del comando 'serverStatus'
                    self.db_parameters= self.db.command('serverStatus')
                    print(f'Host:', self.db_parameters['host'])
                    print(f'Version: ', self.db_parameters['version']) 
                    print(f'Collections:', self.test_client.list_database_names())
                    print(self.db.list_collection_names())
                except Exception as e:
                    print(e)    

            elif parametro=='2':

                #Nombre del fichero sin extension
                inputUser=input('Introduce el nombre del fichero json que desea subir sin su extension: ')
                with open (f'{inputUser}.json','r') as JSONFichero:
                    contenido=f'{JSONFichero.read()}'
                serializarJSON=json.loads(contenido)
                subir_datos=self.col_name.insert_one(serializarJSON)      
                return self.test_client
                
                
            elif parametro=='3':
                __mostrarFichero=[x for x in self.col_name.find()]
                print(__mostrarFichero)

            elif parametro=='4':

                elemento=dict()
                __inputUser=input('Introduce el numero del elemento que deseas eliminar: ')
                elemento=self.col_name.find({f'Elemento':int(__inputUser)})
                print(elemento)
                for x in elemento:
                    self.col_name.delete_one(x)
            
            elif parametro=='5':
                
                __inputUserUpdate=input('Introduce el numero del elemento que deseas actualizar: ')
                elementoActualizar= self.col_name.find({f'Elemento':int(__inputUserUpdate)})
                for i in elementoActualizar:
                    print(i)
                    inputCampo=input('Introduce el nombre del campo que quiere actualizar o añadir: ')
                    inputCampoValor=input('Introduce el valor del campo que quiere actualizar o anadir: ')
                    campoActualizar={"$set": {f'{inputCampo}':int(inputCampoValor)}}
                    self.col_name.update_one(i, campoActualizar)
            
            elif parametro=='0':
                self.test_client.close()
                print('Conexion finalizada.')
                
            
            
            
            

                
            
        

        


if __name__=='__main__':

    ejecute= FirstStepsMongoDB()
    ejecute.main()