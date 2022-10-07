class excepciones():
    def comprobar():
        numero = 7/0
        try :
            print(numero)
        except ZeroDivisionError:
            print("Error, no se puede dividir por 0")

excepciones.comprobar()
