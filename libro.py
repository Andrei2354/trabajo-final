from autor import Autor
from comentario import Comentario

class Libro:
    def __init__(self, id:int , libro:str, comentario:Comentario, autor:Autor):
        self.libro = libro
        self.comentario = comentario
        self.autor = autor
        self.id = int(id)
    
    def actualizar(self, libro:str, autor, comentario):
        self.autor = autor
        self.libro = libro
        self.comentario = comentario
    
    def delete(self) -> None:
        self.autor = None
        self.libro = None
        self.comentario = None

    def __str__(self) -> str:
        return str(self.libro) + "|" + str(self.autor) + "|" + str(self.comentario)
    
    def leer(self) -> str:
        return str(self.id) + "|" + str(self.libro)  + "|" + str(self.autor)  + "|" + str(self.comentario)