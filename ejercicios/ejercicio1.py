class Alumno:
    def __init__(self, nombre, apellido, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota
    def __str__(self):
        return f'El alumno se llama: {self.nombre} {self.apellido} y ha sacado un {self.nota}'
    def crear_alumno(self):
        nombre = str(input('Nombre: '))
        apellido = str(input('Apellido: '))
        nota = int(input('Nota: '))
        print("Se ha creado el alumno con éxito")
        print(Alumno(nombre, apellido, nota))
    def calificacion(self):
        if self.nota >= 5:
            print('Aprobado')
        else:
            print('Suspenso')

alumno = Alumno('Diego', 'de Santos', 7)
alumno.calificacion()

