class Autor:
    def __init__(self, id:int, nombre:str):
        self.id = int(id)
        self.nombre = nombre

    def update(self, nombre):
        self.nombre = nombre

    def delete(self):
        self.nombre = None
    
    def read(self) -> str:
        return str(self.id) + "|" + str(self.nombre)
    
    def __str__(self) -> str:
        return str(self.nombre)