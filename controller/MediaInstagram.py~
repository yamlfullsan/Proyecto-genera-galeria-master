# coding=utf-8
from instagram import InstagramAPIError, InstagramAPI
from httplib2 import ServerNotFoundError
from controller.Peticiones import Peticiones


class BusquedaMedia:

    def __init__(self, token):
        self.__access_token__ = token
        self.__iniciar_conexion__()

    def __iniciar_conexion__(self):
        try:
            self.api = InstagramAPI(access_token=self.__access_token__)
        except Exception, e:
            print('Error Instagram: ' + str(e))
            Peticiones.log_instagram(str(e))

    def media_popular(self, numero_media=1000):

        """
        Obtiene una lista con la Media que es popular
        :param numero_media: Numero maximo de media (por si hay mas) que se queire obtener
        :rtype: list
        """
        if numero_media is None:
            numero_media = Peticiones.es_numero(raw_input('Número de imagenes (Máximo 60): '))

        try:
            lista_media = self.api.media_popular(count=numero_media)

            if len(lista_media) is not 0:
                return self.__guardar_datos_lista_media(lista_media)
            else:
                print('No se encontro media popular')
                return lista_media
        except InstagramAPIError, e:
            print('Error generado por el ApiInstagram al obtener Media Popular: {0}'.format(str(e.message)))
        except Exception, e:
            Peticiones.log_instagram(str(e))

    def por_tag(self, tag):
        """
        Obtiene una lista de Media al buscar por un tag
        :param tag: Tag con el que se buscaran datos
        :rtype: list
        """
        try:
            lista_media = self.api.tag_recent_media(count=1000, tag_name=tag)
            if len(lista_media) is not 0:
                return self.__guardar_datos_lista_media(lista_media[0])  # Solo deuelve el que contiene media
            else:
                print('No se encontraron imagenes con ese tag.')
                return lista_media
        except InstagramAPIError, e:
            print('Error generado por el ApiInstagram al obtener Media Por Tag: {0}'.format(str(e.message)))
        except ServerNotFoundError, e:
            print("Error de servidor: {0}".format(str(e.message)))
            return None
        except Exception, e:
            Peticiones.log_instagram(str(e))

    def por_coordenadas(self, latitud=19.32590558, longitud=-99.18214):

        """
        Obtiene una lista de objetos tipo Media buscando por coordenadas
        :param latitud: Latitud
        :param longitud: Longitud
        :rtype: list
        """
        try:
            lista_media = self.api.media_search(lat=latitud, lng=longitud)

            if len(lista_media) is not 0:
                return self.__guardar_datos_lista_media(lista_media)
            else:
                print('No se encontraron imagenes en ese lugar')
                return lista_media
        except InstagramAPIError, e:
                print('Error generado por el ApiInstagram al obtener Media Por Location: {0}'.format(e.message))
        except Exception, e:
            Peticiones.log_instagram(str(e))

    def __guardar_datos_lista_media(self, lista_media):
        lista = []
        for elemento in lista_media:
            lista.append(self.__obtener_datos__tupla(elemento))
        return lista

    @staticmethod
    def __obtener_datos__diccionario(media):
        datos = \
            {
                'url': media.images['low_resolution'].url,
                'usuario': media.user.username,
                'fecha': media.created_time,
                'descripcion': media.caption,
                'tags': media.filter
            }
        return datos

    def __obtener_datos__tupla(self, media):
        datos = \
            (
                media.images['low_resolution'].url,
                self.__extraer_username__(media),
                self.__extraer_texto__(media),
                media.filter,
                int(media.created_time.day),
                int(media.created_time.month),
                int(media.created_time.year),
                int(media.created_time.hour),
                int(media.created_time.minute),
                int(media.created_time.second),
                str(media.link)[7:]
                )
        return datos

    @staticmethod
    def __extraer_texto__(media):
        try:
            return media.caption.text.encode('utf-8')
        except Exception, e:
            Peticiones.log_instagram(str(e))
            return 'Sin texto'

    @staticmethod
    def __extraer_username__(media):
        username = str(media.user.username)
        return username.title()
