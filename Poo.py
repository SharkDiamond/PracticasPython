#Importaciones

class Carro():
    

    def __init__(self,ColorCarro,MarcaCarro):
        
        self.__Color=ColorCarro
        self.__MarcaCarro=MarcaCarro
        self.__Encendido=False

    def cambiarEstado(self):
        
        if self.Encendido:
            
            self.Encendido=False

        else:
        
            self.Encendido=True    


    def setColor(self,valor):
                
        self.Color=valor

    def setMarca(self,valor):
                
        self.Marca=valor

    def getColor(self):
        
        return self.Color

    def getMarca(self):
        
        return self.Marca



x=Carro()

print(x.Color)

print(x.cambiarEstado())

print(x.Encendido)
