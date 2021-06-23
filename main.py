import os
import re
from PIL import Image, ImageDraw

imagenes_dir = os.path.abspath(os.getcwd())

with os.scandir(imagenes_dir) as ficheros:
    ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.webp') or fichero.name.endswith('.jpg')]

for archivo in ficheros:
    print(archivo)
    imagen = Image.open(archivo)
    
    #Crear cuadrado

    draw = ImageDraw.Draw(imagen)
    draw.rectangle(((0, 00), (200, 200)), fill="#FFFFFF")

    # Aquí hacemos la conversión
    imagen.save(archivo)
 
print("### imagenes listas ####")
# ¡Listo!