from listaautores import ListaAutores
from listalibros import ListaLibros
from listacomentarios import ListaComentarios

class ProveedorAutoresI:
    def getAutores(self)->ListaAutores:
        pass

    def close(self):
        pass

class ProveedorLibrosI:
    def getFrases(self)->ListaLibros:
        pass

    def close(self):
        pass

class ProveedorComentariosI:
    def getFrases(self)->ListaComentarios:
        pass

    def close(self):
        pass