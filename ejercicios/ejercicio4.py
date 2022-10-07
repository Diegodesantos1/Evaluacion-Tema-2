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

excepciones.comprobar() ; excepciones.comprobar2()
