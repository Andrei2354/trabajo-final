import sqlite3

from proveedor1 import ProveedorLibrosI
from listalibros import ListaLibros
from libro import Libro

from database import Database

class ProveedorLibrosSQL(ProveedorLibrosI):
    def __init__(self) -> None:
        self.db = Database()

    def getLibros(self) -> ListaLibros:
        listas_libros = ListaLibros()
        cursor = self.db.getAll('libro')
        for row in cursor:
            libro = Libro(row[0], row[1], row[2])
            listas_libros.create(libro)
        
        self.db.close()
        return listas_libros
    
    def createLibro(self, libro) -> Libro:
        self.db.insert('libro', '(?, ?, ?, ?)', (int(libro.id), str(libro.libro), str(libro.autor), str(libro.comentario)))
        
        return libro
    
    def updateLibro(self, libro:Libro, nuevo_libro:str, nuevo_autor:str, nuevo_comentario:str) -> Libro:
        self.db.update('libro', 'libro=?', 'autor=?', 'comentario=?', (nuevo_libro, nuevo_autor, nuevo_comentario, libro.libro, libro.autor, libro.comentario))
        
        return libro
    
    def deleteLibro(self, libro:Libro) -> Libro:
        self.db.delete('libro', 'libro=?', (libro.libro,))
        
        return libro
    
    def close(self, lista) -> None:
        pass