class Autor:
    def __init__(self, id:int, nombre:str):
        self.id = int(id)
        self.nombre = nombre

    def actualizar(self, nombre):
        self.nombre = nombre

    def borrar(self):
        self.nombre = None
    
    def leer(self) -> str:
        return str(self.id) + "|" + str(self.nombre)
    
    def __str__(self) -> str:
        return str(self.nombre)