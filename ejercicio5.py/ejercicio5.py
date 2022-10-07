class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

coche = Coche("azul", 4, 150, 1200)
print(f"El coche tiene estas características {coche}")
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self) + ", {}".format(self.tipo)

bicicleta = Bicicleta("Verde claro", 2, "montaña")
print(f"La bicicleta tiene estas características {bicicleta}")

class Furgoneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        Vehiculo.__init__(self, color, ruedas)
        self.carga = carga
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} kg".format(self.carga)

Furgoneta = Furgoneta("Roja y blanca", 4, 3000)
print(f"La Furgoneta tiene estas características {Furgoneta}")

def catalogar(vehiculos):
    for i in vehiculos:
        print(i.__class__.__name__, i.__dict__) #codigo de stackoverflow

catalogar([coche, bicicleta, Furgoneta])


