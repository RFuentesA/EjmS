class GameEntry():
    def __init__(self, nombre, puntaje):
        self.__nombre = nombre
        self.__puntaje = puntaje
        
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setPuntaje(self, puntaje):
        self.__puntaje = puntaje
    
    def getPuntaje(self):
        return self.__puntaje

    def __str__(self):
        return "Nombre: "+str(self.__nombre)+" Puntaje: "+str(self.__puntaje)