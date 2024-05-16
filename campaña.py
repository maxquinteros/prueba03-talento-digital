from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoError

class Campaña:

    def __init__(
        self,
        nombre: str,
        fecha_inicio: str,
        fecha_termino: str,
        numero_videos: int,
        numero_displays: int,
        numero_socials: int,
    ):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__videos = []
        self.__displays = []
        self.__socials = []

        for _ in range(numero_videos):
            self.__videos.append(Video())

        for _ in range(numero_displays):
            self.__displays.append(Display())

        for _ in range(numero_socials):
            self.__socials.append(Social())

    def __str__(self):
        return f"Nombre de la campaña: {self.__nombre}\n{self.anuncios}"

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        try:
            if len(value) <= 250:
                self.__nombre = value
            else:
                raise LargoExcedidoError("El nombre excede los carácteres permitidos")
        except LargoExcedidoError as e:
            print(f"Error: {e}")
            with open("error.log", "wt", encoding="utf-8") as stream:
                stream.write(f"{e}")

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value: str):
        self.__fecha_inicio = value

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, value: str):
        self.__fecha_termino = value

    @property
    def anuncios(self):
        return f"Anuncios: {len(self.__videos)} Video, {len(self.__displays)} Display, {len(self.__socials)} Social"
