import io
import pickle

class Persona():


    def __init__(self, nombre, genero, edad):

        self.__nombre = nombre
        self.__genero = genero
        self.__edad = edad
        print("se ha creado una persona con nombre:", self.__nombre)


    def __str__(self):

        return  "{}  {}  {}".format(self.__nombre,self.__genero,self.__edad)

class ListaPersonas():

    personas=[]

    def __init__(self,arg):

        listaDepersonas=open("ficheroExterno","ab+")
        listaDepersonas.seek(0)



    def mostrarPersonas(self):
        for value in self.personas:
            print(value)

    def guardarPersonasEnFichero(self):
        listaDepersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas,listaDepersonas)
        listaDepersonas.close()
        del(listaDepersonas)

    def agregarPersonas(self, *p):
        for valores in p:
            self.personas.append(valores)


miLista=ListaPersonas()

p1=Persona("Raquel","M",21)
p2=Persona("Sergio","M",28)
p3=Persona("Fernada","F",29)
p4=Persona("Albanis","F",23)
p5=Persona("Gabriel","M",34)

miLista.mostrarPersonas()

miLista.agregarPersonas(p1,p2,p3,p4,p4)
