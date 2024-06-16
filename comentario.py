class Comentario:
    def __init__(self, id:int, comentario:str):
        self.id = int(id)
        self.comentario = comentario

    def actualizar(self, comentario):
        self.comentario = comentario

    def borrar(self):
        self.comentario = None
    
    def leer(self) -> str:
        return str(self.id) + "|" + str(self.comentario)
    
    def __str__(self) -> str:
        return str(self.comentario)