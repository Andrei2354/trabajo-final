from autor import Autor

class ListaAutores:
    def __init__(self):
        self.autores = []

    def create(self, autor)->Autor:
        self.autores.append(autor)
        return autor

    def read(self)->list:
        return self.autores
    
    def __str__(self)->str:
        result = ""
        for autor in self.autores:
            result += str(autor) + "\n"
        return result
    
    def getAutor(self, nombre:str)->Autor:
        for autor in self.autores:
            if autor.nombre == nombre:
                return autor
        return None
    
    def getAutorPorId(self, id:int)->Autor:
        for autor in self.autores:
            if int(autor.id) == int(id):
                return autor
        return None

    def update(self, nombre:str, nuevo_nombre:str):
        for autor in self.autores:
            if autor.nombre == nombre:
                autor.update(nuevo_nombre)
                return autor
        return None

    def delete(self, nombre:str):
        for autor in self.autores:
            if autor.nombre == nombre:
                autor.delete()
                self.autores.remove(autor)
                return autor
        return None
    
    def getNewId(self) -> int:
        max_id = 0
        for autor in self.autores:
            if autor.id > max_id:
                max_id = autor.id
        return max_id + 1