class Alumno:
    def __init__(self, nombre, apellido, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota
    def __str__(self):
        return f'El alumno se llama: {self.nombre} {self.apellido} y ha sacado un {self.nota}'
    def crear_alumno():
        nombre = str(input('Nombre: '))
        apellido = str(input('Apellido: '))
        nota = int(input('Nota: '))
        print(Alumno(nombre, apellido, nota))

Alumno.crear_alumno()
