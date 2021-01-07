#Importaciones

class Carro():
    
    Color="naranja"
    Marca=""
    Encendido=False


    def cambiarEstado(self):
        
        if self.Encendido:
            
            self.Encendido=False

        else:
        
            self.Encendido=True    


x=Carro()

print(x.Color)

print(x.cambiarEstado())

print(x.Encendido)
