# coding=utf-8
from TwitterSearch import *
from controller.Peticiones import Peticiones


class MediaTwitter:

    def __init__(self, datos_app):
        # Guarda los datos necesarios para el API
        self.consumer_key = datos_app['c_key']
        self.consumer_secret = datos_app['c_secret']
        self.access_token = datos_app['token']
        self.access_token_secret = datos_app['token_secret']
        self.__iniciar_conexion__()  # Realiza la instancia del API
        self.sin_media = 0  # Contador para los tweets sin imagen

    def __iniciar_conexion__(self):
        try:
            # Crea la instancia del API TwitterSearch
            self.apiTS = TwitterSearch(
                consumer_key=self.consumer_key,
                consumer_secret=self.consumer_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret)
        except Exception, e:
            print('Error Twitter : ' + str(e))
            Peticiones.log_twitter(str(e))  # Guarda error en el log

    def buscar_por_tags(self, tag):
        try:
            tags = [tag]  # Guarda tag en una lista
            tso = TwitterSearchOrder()  # Crea objeto para realizar la búsqueda
            tso.set_keywords(tags)  # Guarda palabras que buscará
            tso.set_include_entities(True)  # True para tweet con toda su información
            tweets = self.apiTS.search_tweets_iterable(tso)  # Realiza la búsqueda
            lista = self.generar_lista_tweets(tweets=tweets)  # Genera la lista con los tweets que tienen imagen
            if len(lista) is not 0:
                return lista # Devuelve la lista si no esta vacía
            print('No hay imagenes en Twitter con ese Hashtag :(')  # Si está vacía muestra mensaje
        except TwitterSearchException as e:
            print('Error Twitter: ' + str(e))
            Peticiones.log_twitter(str(e))  # Guarda mensaje en el log

    def buscar_por_cordenadas(self, latitud, longitud):
        try:
            tso = TwitterSearchOrder()  # Crea objeto de búsqueda
            tso.set_keywords(['a'])  # Palabras con las que buscará
            tso.set_include_entities(True)  # Tweet con todos los datos Verdadero
            tso.set_geocode(latitud, longitud, 5000, imperial_metric=False)  # Coordenadas y radio de busqueda en Km
            tso.set_result_type('mixed')  # Tipo de búsqueda mezcla de todo
            tweets = self.apiTS.search_tweets_iterable(tso)  # Realiza la búsqueda y guarda los tweets
            lista = self.generar_lista_tweets(tweets)  # Genera la lista con los datos de los tweets
            if len(lista) is not 0:
                return lista  # Si la lista no esta vacía la devuelve
            print('No hay imagenes en Twitter con esas coordenadas :(')  # Si no hubo tweets muestra mensaje
        except TwitterSearchException as e:
            print('Error Busqueda por Coordenadas twitter: ' + str(e))
        except Exception, e:
            print('Error al realizar la busqueda Twitter: ' + str(e))
            Peticiones.log_twitter(str(e))  # Guarda el error en el Log

    def buscar_popular(self):
        try:
            tso = TwitterSearchOrder()  # Crea objeto de búsqueda
            tso.set_keywords(['mexico']) # Palabra que buscará
            tso.set_include_entities(True)  # Tweet con toda la información disponible Verdadero
            tso.set_result_type('popular')  # Tipo de búsqueda tweets populares
            tweets = self.apiTS.search_tweets_iterable(tso)  # Realiza la busqueda
            lista = self.generar_lista_tweets(tweets=tweets)  #
            if len(lista) is 0:
                print('No hay imagenes en Twitter (Popular) :(')
                return None  # Si la lista esta vacía devuelve None
            return lista  # Si hubo tweets devuelve la lista con los datos
        except TwitterSearchException as e:
            print('Error twitter : ' + str(e))
            Peticiones.log_twitter(str(e))

    def generar_lista_tweets(self, tweets):
        lista = []
        count = 0  # Para detener la búsqueda
        for tweet in tweets:
            datos = self.extraer_datos_tupla(tweet)  # Extrae los datos
            if datos is not None:
                lista.append(datos)  # Si hubo datos los agrega a la lista
            if count == 2000:
                break  # Busca sólo en 2000 tweets
            count += 1
        return lista  # Devuelve la lista con los datos

    def extraer_datos_tupla(self, tweet):
        try:
            lista = tweet['entities']['media']  # Extrae una lista de dos diccionarios si contiene imagen el tweet
            dic = lista[0]  # Obtenemos el primer diccionario, que trae la información que necesitamos
            fecha = self.obtener_fecha(tweet['created_at'])  # Obtiene la fecha
            hora = self.obtener_hora(tweet['created_at']) # Obtiene la hora
            tupla_datos = (
                str(dic['media_url'].encode('utf-8')),  # Obtiene la url de la imagen
                tweet['user']['name'].encode('utf-8').title(),  # Obtiene el nombre de usuario
                str(tweet['text'].encode('utf-8')),  # Obtiene el texto del tweet
                str(tweet['user']['description'].encode('utf-8')),  # Obtiene la descripción del usuario
                fecha[0],  # Día
                fecha[1],  # Mes
                fecha[2],  # Año
                hora[0],  # Hora
                hora[1],  # Minuto
                hora[2],  # Segundo
                str(tweet['entities']['media'][0]['display_url'])  # Obtiene el url a la pagina del tweet en twitter
            )
            return tupla_datos
        except Exception, e:
            self.sin_media += 1
            Peticiones.log_twitter(str(e))  # Guarda error el el Log
            return None

    @staticmethod
    def cambio_mes(mes):
        # Cambia el dato del mes de palabra a número
        if mes == 'Jan':
            return 1
        elif mes == 'Feb':
            return 2
        elif mes == 'Mar':
            return 3
        elif mes == 'Apr':
            return 4
        elif mes == 'May':
            return 5
        elif mes == 'Jun':
            return 6
        elif mes == 'Jul':
            return 7
        elif mes == 'Aug':
            return 8
        elif mes == 'Sep':
            return 9
        elif mes == 'Oct':
            return 10
        elif mes == 'Nov':
            return 11
        elif mes == 'Dec':
            return 12

    def obtener_fecha(self, fecha):
        # Obtiene la fecha del tweet y divide sus partes en una tupla
        lista = fecha.split(' ')
        fecha = (
            int(lista[2]),
            self.cambio_mes(lista[1]),
            int(lista[5])
            )
        return fecha

    @staticmethod
    def obtener_hora(fecha):
        # Obtiene la hora y divide sus partes en una tupla
        lista = fecha.split(' ')
        h = lista[3].split(':')
        hora = (int(h[0]), int(h[1]), int(h[2]))
        return hora
