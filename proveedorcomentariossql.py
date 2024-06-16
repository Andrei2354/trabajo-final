import sqlite3

from proveedor1 import ProveedorComentariosI
from listacomentarios import ListaComentarios
from comentario import Comentario

from database import Database


class ProveedorComentarioSQL(ProveedorComentariosI):
    def __init__(self):
        self.db = Database()

    def getComentarios(self):
        lista_comentarios = ListaComentarios()
        cursor = self.db.getAll('comentario')
        for row in cursor:
            comentario = Comentario(row[0], row[1])
            lista_comentarios.create(comentario)

        self.db.close()
        return  lista_comentarios
    
    def createComentario(self, comentario):
        self.db.insert('comentario', '(?, ?)', (int(comentario.id), str(comentario.nombre)))

        return comentario
    
    def updateComentario(self, nombre, nuevo_nombre):
        self.db.update('comentario', 'nombre=?', 'nombre=?', (nuevo_nombre, nombre))
        
        return Comentario(-1, nuevo_nombre)
    
    def deleteComentario(self, nombre):
        self.db.delete('comentario', 'nombre=?', (nombre,))
        
        return Comentario(-1, nombre)

    def close(self, lista):
        pass