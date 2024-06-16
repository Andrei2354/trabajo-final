from comentario import Comentario

class ListaComentarios:
    def __init__(self):
        self.comentarios = []

    def create(self, comentario)->Comentario:
        self.comentarios.append(comentario)
        return comentario

    def read(self)->list:
        return self.comentarios
    
    def __str__(self)->str:
        result = ""
        for comentario in self.comentarios:
            result += str(comentario) + "\n"
        return result
    
    def getComentario(self, nombre:str)->Comentario:
        for comentario in self.comentarios:
            if comentario.nombre == nombre:
                return comentario
        return None
    
    def getComentarioPorId(self, id:int)->Comentario:
        for comentario in self.comentarios:
            if int(comentario.id) == int(id):
                return comentario
        return None

    def update(self, nombre:str, nuevo_nombre:str):
        for comentario in self.comentarios:
            if comentario.nombre == nombre:
                comentario.update(nuevo_nombre)
                return comentario
        return None

    def delete(self, nombre:str):
        for comentario in self.comentarios:
            if comentario.nombre == nombre:
                comentario.delete()
                self.comentarios.remove(comentario)
                return comentario
        return None
    
    def getNewId(self) -> int:
        max_id = 0
        for comentario in self.comentarios:
            if comentario.id > max_id:
                max_id = comentario.id
        return max_id + 1