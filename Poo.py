#Importaciones



class Carro():
	
	#Propiedades	
	color="naraja"
	Modelo="Ferrari"
	largo="2 Metros"
	Cauchos="Pirelli"
    encendido=False


	#Comportamiento
    def EncenderOapagar(self):

    	if self.encendido:
    		
    		return self.encendido=False
		    print("auto apagado")	
    	
    	else:
    	
    		return self.encendido=True	
    		print("auto encendido")



Focus=Carro();


Focus.EncenderOapagar();

print(Focus.color)


print(Focus.color="Naranja")
	