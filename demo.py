from anuncio import *
from campaña import *
from error import *

campaña1 = Campaña(
    nombre="Mi primera campaña",
    fecha_inicio="",
    fecha_termino="",
    numero_videos=1,
    numero_displays=0,
    numero_socials=0,
)


try:
    campaña1.nombre = input("Ingrese el nombre nuevo de la campaña:\n>")
except LargoExcedidoError as e:
    print(f"Error: {e}")
print(campaña1)