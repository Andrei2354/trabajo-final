class Autor:
    def __init__(self, autor:str) -> None:
        self.autor = autor
    
    def __str__(self) -> str:
        return self.autor
    
    def leer(self) -> str:
        return self.autor
