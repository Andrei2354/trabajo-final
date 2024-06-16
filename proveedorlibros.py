from proveedorlibrossql import ProveedorLibrosSQL
from listalibros import ListaLibros
from libro import Libro

from proveedorautores import ProveedorAutores
from proveedorcomentarios import ProveedorComentarios

class ProveedorLibros:
    def __init__(self, tipo, autosave=False):
        self.proveedorAutores = ProveedorAutores(tipo, autosave)
        self.proveedorComentarios = ProveedorComentarios(tipo, autosave)

        if tipo == 'sql':
            self.proveedor = ProveedorLibrosSQL(self.proveedorAutores)
            self.proveedor = ProveedorLibrosSQL(self.proveedorComentarios)

        self.tipo       = tipo
        self.autosave   = autosave
        self.libros     = self.proveedor.getLibros()

    def getLibros(self)->ListaLibros:
        return self.libros

    def getLibro(self, libro, autor)->Libro:
        return self.libros.getLibro(libro, autor)

    def getLibroPorId(self, id)->Libro:
        return self.libros.getLibroPorId(id)

    def createLibro(self, libro:str, aut:str)->Libro:
        resultado = None
        autor = self.proveedorAutores.getAutor(aut)
        comentario = self.proveedorComentarios.getComentario(aut)
        if autor == None:
            autor = self.proveedorAutores.createAutor(aut)
            self.proveedorAutores.close()
        
        if comentario == None:
            comentario = self.proveedorComentarios.createComentario(aut)
            self.proveedorComentarios.close()

        if (self.getLibro(libro, autor, comentario) == None):
            resultado = self.libros.create(Libro(self.libros.getNewId(), libro, autor, comentario))
        
            if self.tipo == 'sql':
                self.proveedor.createLibro(resultado)

        if self.autosave:
            self.proveedor.close(self.libros)
            self.libros = self.proveedor.getLibros()
        
        return resultado

    def updateLibro(self, libro, autor, comentario, nuevo_libro, nuevo_autor, nuevo_comentario)->Libro:
        resultado = None
        if (self.getLibro(nuevo_libro, nuevo_autor, nuevo_comentario) == None):
            resultado = self.libros.update(libro, autor, comentario, nuevo_libro, nuevo_autor, nuevo_comentario)

            if self.tipo == 'sql':
                self.proveedor.updateLibro(libro, autor, comentario, nuevo_libro, nuevo_autor, nuevo_comentario)
        
        if self.autosave:
            self.proveedor.close(self.libros)
            self.libros = self.proveedor.getLibros()
        
        return resultado

    def deleteLibro(self, libro, autor, cometario)->Libro:
        resultado = self.libros.delete(libro, autor, cometario)
        
        if self.autosave and resultado != None:
            self.proveedor.close(self.libros)
            self.libros = self.proveedor.getLibros()

            if self.tipo == 'sql':
                self.proveedor.deleteLibro(resultado)

    def close(self):
        self.proveedor.close(self.libros)