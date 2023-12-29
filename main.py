import os

def leer_contenido():
    archivos = os.listdir("./carpeta")

    for archivo in archivos:
        with open("./carpeta/"+archivo, "r") as f:
            print(f.readlines())

leer_contenido()