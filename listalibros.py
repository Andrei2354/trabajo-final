from libro import Libro

class ListaLibros:
    def __init__(self):
        self.libros = []

    def create(self, libro)->Libro:
        self.libros.append(libro)
        return libro

    def read(self)->list:
        return self.libros
    
    def __str__(self)->str:
        result = ""
        for libro in self.libros:
            result += str(libro) + "\n"
        return result
    
    def getLibro(self, nombre:str)->Libro:
        for libro in self.libros:
            if libro.nombre == nombre:
                return libro
        return None
    
    def getLibroPorId(self, id:int)->Libro:
        for libro in self.libros:
            if int(libro.id) == int(id):
                return libro
        return None

    def update(self, nombre:str, nuevo_nombre:str):
        for libro in self.libros:
            if libro.nombre == nombre:
                libro.update(nuevo_nombre)
                return libro
        return None

    def delete(self, nombre:str):
        for libro in self.libros:
            if libro.nombre == nombre:
                libro.delete()
                self.libros.remove(libro)
                return libro
        return None
    
    def getNewId(self) -> int:
        max_id = 0
        for libro in self.libros:
            if libro.id > max_id:
                max_id = libro.id
        return max_id + 1