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
        self.__iniciar_conexion__()  
        self.sin_media = 0  

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
            Peticiones.log_twitter(str(e))  

    def buscar_por_tags(self, tag):
        try:
            tags = [tag]  
            tso = TwitterSearchOrder()  
            tso.set_keywords(tags)  
            tso.set_include_entities(True)  
            tweets = self.apiTS.search_tweets_iterable(tso)  
            lista = self.generar_lista_tweets(tweets=tweets)  
            if len(lista) is not 0:
                return lista 
            print('No existe Hashtag ')  
        except TwitterSearchException as e:
            print('Error Twitter: ' + str(e))
            Peticiones.log_twitter(str(e))  

    def buscar_por_cordenadas(self, latitud, longitud):
        try:
            tso = TwitterSearchOrder()  
            tso.set_keywords(['a'])  
            tso.set_include_entities(True)  
            tso.set_geocode(latitud, longitud, 5000, imperial_metric=False)  
            tso.set_result_type('mixed')  
            tweets = self.apiTS.search_tweets_iterable(tso)  
            lista = self.generar_lista_tweets(tweets)  
            if len(lista) is not 0:
                return lista 
            print('sin imagenes :p')  
        except TwitterSearchException as e:
            print('Error Busqueda por Coordenadas twitter: ' + str(e))
        except Exception, e:
            print('Error al realizar la busqueda Twitter: ' + str(e))
            Peticiones.log_twitter(str(e))  

    def buscar_popular(self):
        try:
            tso = TwitterSearchOrder()  
            tso.set_keywords(['mexico']) 
            tso.set_include_entities(True)  
            tso.set_result_type('popular')  
            tweets = self.apiTS.search_tweets_iterable(tso)  
            lista = self.generar_lista_tweets(tweets=tweets)  
            if len(lista) is 0:
                print('No imagenes (Popular) :p')
                return None 
            return lista  
        except TwitterSearchException as e:
            print('Error twitter : ' + str(e))
            Peticiones.log_twitter(str(e))

    def generar_lista_tweets(self, tweets):
        lista = []
        count = 0  
        for tweet in tweets:
            datos = self.extraer_datos_tupla(tweet) 
            if datos is not None:
                lista.append(datos) 
            if count == 2000:
                break  
            count += 1
        return lista  

    def extraer_datos_tupla(self, tweet):
        try:
            lista = tweet['entities']['media']  
            dic = lista[0]  
            fecha = self.obtener_fecha(tweet['created_at'])  
            hora = self.obtener_hora(tweet['created_at']) 
            tupla_datos = (
                str(dic['media_url'].encode('utf-8')), 
                tweet['user']['name'].encode('utf-8').title(),  
                str(tweet['text'].encode('utf-8')),  
                str(tweet['user']['description'].encode('utf-8')),  
                fecha[0],  # Día
                fecha[1],  # Mes
                fecha[2],  # Año
                hora[0],  # Hora
                hora[1],  # Minuto
                hora[2],  # Segundo
                str(tweet['entities']['media'][0]['display_url'])  
            )
            return tupla_datos
        except Exception, e:
            self.sin_media += 1
            Peticiones.log_twitter(str(e))  
            return None

    @staticmethod
    def cambio_mes(mes):
        
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
        
        lista = fecha.split(' ')
        fecha = (
            int(lista[2]),
            self.cambio_mes(lista[1]),
            int(lista[5])
            )
        return fecha

    @staticmethod
    def obtener_hora(fecha):
       
        lista = fecha.split(' ')
        h = lista[3].split(':')
        hora = (int(h[0]), int(h[1]), int(h[2]))
        return hora
