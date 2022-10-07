class Excepciones():
    def menu():
        eleccion=int(input("¿Qué quieres comprobar? 1: división entre 0, 2: índice de lista inexistente, 3: clave de diccionario inexistente, 4: suma de número y letra\n "))
        if eleccion == 1:
            numero = 7/0
            try :
                print(numero)
            except ZeroDivisionError:
                print("Error, no se puede dividir por 0")
        elif eleccion == 2:
            lista = [4, 7, 30, 23, 5]
            lista[10]
            try:
                print(lista[10])
            except IndexError:
                print("Error, no existe elemento con ese índice")
        elif eleccion == 3:
            paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" }
            paises["alemania"]
            try:
                print(paises["alemania"])
            except KeyError:
                print("Error, no existe ese elemento en el diccionario")
        elif eleccion == 4:
            resultado = "2" + 10
            try:
                print(resultado)
            except TypeError:
                print("Error, no puedes sumar números y letras")
        else:
            print("Error, no existe esa opción")
            Excepciones.menu()


Excepciones.menu()

