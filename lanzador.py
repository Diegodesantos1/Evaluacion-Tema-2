import sys
import pathlib
from colorama import Fore

def lanzador():
    eleccion=int(input(Fore.GREEN +"\n\n ¿Qué ejercicio quieres ejecutar? \n \n Pulse 1: Ejercicio 1 \n \n Pulse 2: Ejercicio 2 \n \n Pulse 3: Ejercicio 3 \n\n Pulse 4: Ejercicio 4 \n \n Pulse 5: Ejercicio 5 \n \n Pulse 6 : para salir \n \n" + Fore.RESET))
    if eleccion == 1 or 2:
        sys.path.append(str(pathlib.Path(__file__).parent.absolute()) + "./examen/ejercicio1_2/")
        import ejercicio1_2
        lanzador()
    elif eleccion == 3:
        sys.path.append(str(pathlib.Path(__file__).parent.absolute()) + "./examen/ejercicio3/")
        import ejercicio3
        lanzador()
    elif eleccion == 4:
        sys.path.append(str(pathlib.Path(__file__).parent.absolute()) + "./examen/ejercicio4/")
        import ejercicio4
        lanzador()
    elif eleccion == 5:
        sys.path.append(str(pathlib.Path(__file__).parent.absolute()) + "./examen/ejercicio5/")
        import ejercicio5
        lanzador()
    else:
        sys.exit()
lanzador()