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
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.videos = []
        self.displays = []
        self.socials = []

        for video in range(numero_videos):
            self.videos.append(Video())

        for display in range(numero_displays):
            self.displays.append(Display())

        for social in range(numero_socials):
            self.socials.append(Social())

    def __str__(self):
        return f"Nombre de la campaña: {self.nombre}\n{self.anuncios}"

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        try:
            if len(value) <= 250:
                self._nombre = value
            else:
                raise LargoExcedidoError("El nombre excede los carácteres permitidos")
        except LargoExcedidoError as e:
            print(f"Error: {e}")
            with open("error.log", "wt", encoding="utf-8") as stream:
                stream.write(f"{e}")

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self._fecha_inicio = value

    @property
    def fecha_termino(self):
        return self._fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, value):
        self._fecha_termino = value

    @property
    def anuncios(self):
        return f"Anuncios: {len(self.videos)} Video, {len(self.displays)} Display, {len(self.socials)} Social"
