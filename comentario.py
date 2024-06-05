class Comentario:
    def __init__(self, comentario:str) -> None:
        self.comentario = comentario
    
    def __str__(self) -> str:
        return self.comentario
    
    def leer(self) -> str:
        return self.comentario