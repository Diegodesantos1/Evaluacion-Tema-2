class excepciones():
    def comprobar():
        numero = 7/0
        try :
            print(numero)
        except ZeroDivisionError:
            print("Error, no se puede dividir por 0")
    def comprobar2():
        lista = [4, 7, 30, 23, 5]
        lista[10]
        try:
            print(lista[10])
        except IndexError:
            print("Error, no existe elemento con ese índice")
    def comprobar3():
        paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" }
        paises["alemania"]
        try:
            print(paises["alemania"])
        except KeyError:
            print("Error, no existe ese elemento en el diccionario")

excepciones.comprobar() ; excepciones.comprobar2() ; excepciones.comprobar3()
