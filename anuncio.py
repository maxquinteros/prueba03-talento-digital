from abc import ABC, abstractmethod
from error import SubTipoInvalidoError




class Anuncio:
    def __init__(self, sub_tipo: str, ancho=1, alto=1, url_archivo="", url_clic=""):
        self.ancho = ancho
        self.alto = alto
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos():
        print("VIDEO:")
        print("==========")
        print("- ", end="")
        print("\n- ".join(Video.SUB_TIPOS))
        print("")

        print("DISPLAY:")
        print("==========")
        print("- ", end="")
        print("\n- ".join(Display.SUB_TIPOS))
        print("")

        print("SOCIAL:")
        print("==========")
        print("- ", end="")
        print("\n- ".join(Social.SUB_TIPOS))

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    @property
    def sub_tipo(self) -> str:
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value) -> str:
        try:
            if value in Video.SUB_TIPOS:
                self._sub_tipo = value
            elif value in Display.SUB_TIPOS:
                self._sub_tipo = value
            elif value in Social.SUB_TIPOS:
                self._sub_tipo = value
            else:
                raise SubTipoInvalidoError("Sub tipo no encontrado")

        except Exception as SubTipoInvalidoException:
            print(f"SubTipo Invalido: {SubTipoInvalidoException}")

    @property
    def ancho(self) -> int:
        return self._ancho

    @ancho.setter
    def ancho(self, value: int):
        self._ancho = value if value > 0 else 1

    @property
    def alto(self) -> int:
        return self._alto

    @alto.setter
    def alto(self, value: int):
        self._alto = value if value > 0 else 1

    @property
    def url_archivo(self) -> str:
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, value: int):
        self._url_archivo = value

    @property
    def url_clic(self) -> str:
        return self._url_clic

    @url_clic.setter
    def url_clic(self, value: int):
        self._url_clic = value


class Video(Anuncio):

    SUB_TIPOS = ["instream", "outstream"]

    def __init__(self, duracion=5, url_archivo="", url_clic=""):
        self.ancho = 1
        self.alto = 1
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.duracion = duracion

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

    @property
    def duracion(self) -> int:
        return self._duracion

    @duracion.setter
    def duracion(self, value: int):
        self._duracion = value if value > 0 else 5


class Display(Anuncio):

    SUB_TIPOS = ["tradicional", "native"]

    def __init__(self):
        pass

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):

    SUB_TIPOS = ["facebook", "linkedin"]

    def __init__(self):
        pass

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
