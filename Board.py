from GameEntry import *
class Board():
    def __init__(self, Capacidad):
        self.__nEntradas = 0
        self.__Capacidad = Capacidad
        self.__board = []
    
    def getBoard(self):
        return self.__board
    
    def setNEntradas(self, n):
        self.__nEntradas = n
        
    def getNEntradas(self):
        return self.__nEntradas
        
    def add(self,e):
        nuevo
        self.__board.append(e)
            
    def __str__(self):
        for i in self.getBoard():
            x = (str(i.getPuntaje()))
            return print(x)
         
    
x = Board(3)
a = GameEntry("Ana", 5)
b = GameEntry("bob", 10)
x.add(a)
x.add(b)
s = x.getBoard()
print (s[0], s[1])