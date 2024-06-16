from libro import Libro

class ListaLibros:
    def __init__(self):
        self.libros = []

    def create(self, libro)->Libro:
        if type(libro) != Libro:
            raise TypeError("libro must be a Libro object")

        if libro not in self.libros:
            return self.libros.append(libro)
        return None

    def read(self)->list:
        return self.libros
    
    def __str__(self)->str:
        result = ""
        for libro in self.libros:
            result += str(libro) + "\n"
        return result
    
    def getlibro(self, libro, autor, comentario)->Libro:
        for libro in self.libros:
            if libro.libro == libro and libro.autor == autor and libro.comentario == comentario:
                return libro
        return None
    
    def getlibroPorId(self, id:int)->Libro:
        for libro in self.libros:
            if int(libro.id) == int(id):
                return libro
        return None

    def update(self, libro, autor, comentario, nova_libro, new_autor, new_comentario):
        for libro in self.libros:
            if libro.libro == libro and libro.autor == autor and libro.comentario == comentario:
                libro.update(nova_libro, new_autor, new_comentario)
                return libro
        return None

    def delete(self, libro, autor, comentario):
        for libro in self.libros:
            if libro.libro == libro and libro.autor == autor and libro.comentario == comentario:
                self.libros.remove(libro)
                return libro
        return None
    
    def getNewId(self) -> int:
        max_id = 0
        for libro in self.libros:
            if libro.id > max_id:
                max_id = libro.id
        return max_id + 1