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
        for l in self.libros:
            result += str(l) + "\n"
        return result
    
    def getLibro(self, libro, autor, comentario)->Libro:
        for l in self.libros:
            if l.libro == libro and l.autor == autor and l.comentario == comentario:
                return l
        return None
    
    def getLibroPorId(self, id:int)->Libro:
        for l in self.libros:
            if int(l.id) == int(id):
                return l
        return None

    def update(self, libro, autor, comentario, nuevo_libro, nuevo_autor, nuevo_comentario):
        for l in self.libros:
            if l.libro == libro and l.autor == autor and l.comentario == comentario:
                l.update(nuevo_libro, nuevo_autor, nuevo_comentario)
                return l
        return None

    def delete(self, libro, autor, comentario):
        for l in self.libros:
            if l.libro == libro and l.autor == autor and l.comentario == comentario:
                self.libros.remove(l)
                return l
        return None
    
    def getNewId(self) -> int:
        max_id = 0
        for l in self.libros:
            if l.id > max_id:
                max_id = l.id
        return max_id + 1