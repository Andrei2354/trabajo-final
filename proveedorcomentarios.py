from proveedorcomentariossql import ProveedorComentarioSQL
from listacomentarios import ListaComentarios
from comentario import Comentario

class ProveedorComentarios:
    def __init__(self, tipo:str, autosave:bool=False):
        if tipo == 'sql':
            self.proveedor = ProveedorComentarioSQL()

        self.tipo       = tipo
        self.autosave   = autosave
        self.comentarios    = self.proveedor.getComentarios()

    def getComentarios(self)->ListaComentarios:
        return self.comentarios
    
    def getComentario(self, nombre:str)->Comentario:
        return self.comentarios.getComentario(nombre)

    def getComentarioPorId(self, id:int)->Comentario:
        return self.comentarios.getComentarioPorId(id)

    def createComentario(self, nombre:str)->Comentario:
        resultado = None
        if (self.getComentario(nombre) == None):
            resultado = self.comentarios.create(Comentario(self.comentarios.getNewId(), nombre))
        
            if self.tipo == 'sql':
                self.proveedor.createComentario(resultado)

        if self.autosave:
            self.proveedor.close(self.comentarios)
            self.comentarios = self.proveedor.getComentarios()
        
        return resultado

    def updateComentario(self, nombre:str, nuevo_nombre:str)->Comentario:
        resultado = None
        if (self.getComentario(nuevo_nombre) == None):
            resultado = self.comentarios.update(nombre, nuevo_nombre)

            if self.tipo == 'sql':
                self.proveedor.updateComentario(nombre, nuevo_nombre)
        
        if self.autosave:
            self.proveedor.close(self.comentarios)
            self.comentarios = self.proveedor.getComentarios()
        
        return resultado

    def deleteComentario(self, nombre:str)->Comentario:
        resultado = self.comentarios.delete(nombre)
        
        if self.autosave and resultado != None:
            self.proveedor.close(self.comentarios)
            self.comentarios = self.proveedor.getComentarios()

            if self.tipo == 'sql':
                self.proveedor.deleteComentario(str(nombre))

        return resultado

    def close(self):
        self.proveedor.close(self.comentarios)