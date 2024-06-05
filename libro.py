class Libro:
    def __init__(self, libro:str) -> None:
        self.libro = libro
    
    def __str__(self) -> str:
        return self.libro
    
    def leer(self) -> str:
        return self.libro