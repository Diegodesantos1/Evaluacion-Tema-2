class Producto:
    def __init__(self, nombre, precio, codigo, tipo):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
        self.tipo = tipo
    def __str__(self):
        return self.nombre + str(self.precio) + str(self.codigo) + self.tipo

def ejecutar3():
    Producto1 = Producto("Coca-Cola", 1.5, 1234, "Bebida")
    Producto2 = Producto("Martillo", 3.5, 45637, "Herramienta")
    print(Producto1) ; print(Producto2)
ejecutar3()

