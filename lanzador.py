import sys
from colorama import Fore

def lanzador():
    eleccion=int(input(Fore.GREEN +"\n\n ¿Qué ejercicio quieres ejecutar? \n \n Pulse 1: Ejercicio 1 \n \n Pulse 3: Ejercicio 3 \n\n Pulse 4: Ejercicio 4 \n \n Pulse 5: Ejercicio 5 \n \n Pulse 6 : para salir \n \n" + Fore.RESET))
    if eleccion == 1:
        import examen.ejercicio1_2
        lanzador()
    elif eleccion == 3:
        import examen.ejercicio3
        lanzador()
    elif eleccion == 4:
        import examen.ejercicio4
        lanzador()
    elif eleccion == 5:
        import examen.ejercicio5
        lanzador()
    else:
        sys.exit()
lanzador()