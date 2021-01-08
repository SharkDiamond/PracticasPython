#Importaciones

class Carro():
    

    def __init__(self,ColorCarro,MarcaCarro):
        
        self.__Color=ColorCarro
        self.__MarcaCarro=MarcaCarro
        self.__Encendido=False

    def cambiarEstado(self):
        
        if self.__Encendido:
            
            self.__Encendido=False

        else:
        
            self.__Encendido=True    


    def setColor(self,valor):
                
        self.__Color=valor

    def setMarca(self,valor):
                
        self.__Marca=valor

    def getColor(self):
        
        return self.__Color

    def getMarca(self):
        
        return self.__Marca


x=Carro("Azul","Lambo")

print(x.getColor())

print(x.cambiarEstado())

