class Comentario:
    def __init__(self, id:int, comentario:str):
        self.id = int(id)
        self.comentario = comentario

    def update(self, comentario):
        self.comentario = comentario

    def delete(self):
        self.comentario = None
    
    def read(self) -> str:
        return str(self.id) + "|" + str(self.comentario)
    
    def __str__(self) -> str:
        return str(self.comentario)