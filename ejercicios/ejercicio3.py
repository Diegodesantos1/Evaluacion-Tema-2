class Producto:
    def __init__(self, nombre, precio, codigo, tipo):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
        self.tipo = tipo
    def __str__(self):
        return self.nombre + ": " + str(self.precio)