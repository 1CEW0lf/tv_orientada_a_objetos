import time
import os
from tv import TV

television1 = TV("Sony", 56)

while True:
    print(television1.estatus_actual())
    print("Control remoto")
    print("1. Encender")
    print("2. Subir Volumen")
    print("3. Bajar Volumen")
    print("4. Cambiar Canal")
    boton = input("Presiona un botón: ")
    if boton == "1":
        television1.power()
    elif boton == "2":
        television1.cambiar_volumen(1)
    elif boton == "3":
        television1.cambiar_volumen(-1)
    
    time.sleep(1)
    print(television1.estatus_actual())
    input("Presiona enter para continuar...")
    os.system("clear")
