from proveedorautoressql import ProveedorAutoresSQL
from listaautores import ListaAutores
from autor import Autor

class ProveedorAutores:
    def __init__(self, tipo:str, autosave:bool=False):
        if tipo == 'sql':
            self.proveedor = ProveedorAutoresSQL()

        self.tipo       = tipo
        self.autosave   = autosave
        self.autores    = self.proveedor.getAutores()

    def getAutores(self)->ListaAutores:
        return self.autores

    def getAutor(self, nombre:str)->Autor:
        return self.autores.getAutor(nombre)

    def getAutorPorId(self, id:int)->Autor:
        return self.autores.getAutorPorId(id)

    def createAutor(self, nombre:str)->Autor:
        resultado = None
        if (self.getAutor(nombre) == None):
            resultado = self.autores.create(Autor(self.autores.getNewId(), nombre))
        
            if self.tipo == 'sql':
                self.proveedor.createAutor(resultado)

        if self.autosave:
            self.proveedor.close(self.autores)
            self.autores = self.proveedor.getAutores()
        
        return resultado

    def updateAutor(self, nombre:str, nuevo_nombre:str)->Autor:
        resultado = None
        if (self.getAutor(nuevo_nombre) == None):
            resultado = self.autores.update(nombre, nuevo_nombre)

            if self.tipo == 'sql':
                self.proveedor.updateAutor(nombre, nuevo_nombre)
        
        if self.autosave:
            self.proveedor.close(self.autores)
            self.autores = self.proveedor.getAutores()
        
        return resultado

    def deleteAutor(self, nombre:str)->Autor:
        resultado = self.autores.delete(nombre)
        
        if self.autosave and resultado != None:
            self.proveedor.close(self.autores)
            self.autores = self.proveedor.getAutores()

            if self.tipo == 'sql':
                self.proveedor.deleteAutor(str(nombre))

        return resultado

    def close(self):
        self.proveedor.close(self.autores)