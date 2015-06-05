#!/usr/bin/env python
# coding=utf-8

from controller.Peticiones import Peticiones
from controller.MediaInstagram import BusquedaMedia
from controller.MediaTwitter import MediaTwitter
from model.GeneradorHTML import GeneradorHTML
from controller.Ordenacion import OrdenadorImagenes
from termcolor import *


# Clase Run, combinación de los componenetes y generar el programa
class Run:
    def __init__(self):
        print('espera ... :p... :D... procesando...')  
        self.lista_imagenes = []  
        self.token_instagram = '451099039.aca0ba1.fb54f08da95e48289c9d8487afdd5bd2'  # Access Token de Instagram
        self.datos_twitter = {
            'c_key': 'NBN1p3E3LCAL09HEDB1iLxLJy',
            'c_secret': 'ln84qQMz1sjFx4XcQ6lweiTRNdVMEfK3y7wgU0AjZ4GhoWdVKq',
            'token': '247591112-VMDzDUlniPGuT7uDZDLGOESMKEpXNCYh7i836fUX',
            'token_secret': 'YDz2Yn9YNHMlmKRiWYHIBxn5DXviODfVYRSHqVMSZvqQW'
            }  # Diccionario con los datos de Twitter
        self.search_t = MediaTwitter(self.datos_twitter)  
        self.search_i = BusquedaMedia(self.token_instagram)  

    def menu_busqueda(self):
        Peticiones.limpiar_pantalla()  
        cprint('\t\t\tinstagran y twitter', 'green', attrs=['bold'])  
        self.__menu_tipo_busqueda__()  
        modo_busqueda = Peticiones.pedir_numero('Escoge la acción que desees realizar: ', 1, 3)  
        if modo_busqueda is 1:
            self.__busqueda_tag__()  
        elif modo_busqueda is 2:
            self.__busqueda_popular__()  
        else:
            self.__busqueda_coordenadas__()  
        self.generar_html()  

    def __busqueda_tag__(self):
        tag = raw_input('Escribe un Hashtag :D (sin #)... : ')  
        print('espera ... :p... :D... procesando...')  
        self.__agregar_imagenes__(self.search_i.por_tag(tag))  

        self.__agregar_imagenes__(self.search_t.buscar_por_tags(tag))  

    def __busqueda_popular__(self):
        print('espera ... :p... :D... procesando...') 
        self.__agregar_imagenes__(self.search_i.media_popular())  

        self.__agregar_imagenes__(self.search_t.buscar_popular())  

    def __busqueda_coordenadas__(self):
        print('Mapa: http://www.bufa.es/google-maps-latitud-longitud/')  
        latitud = float(raw_input('\tLat: '))  
        longitud = float(raw_input('\tLong: '))  
        print('espera ... :p... :D... procesando...')  
        self.__agregar_imagenes__(self.search_i.por_coordenadas(latitud, longitud))  

        self.__agregar_imagenes__(self.search_t.buscar_por_cordenadas(latitud, longitud))  

    def __agregar_imagenes__(self, lista_datos):

        
        if lista_datos is not None:
            for datos in lista_datos: 
                self.lista_imagenes.append(datos)  

    def generar_html(self):
        Peticiones.limpiar_pantalla()  
        ordenador = OrdenadorImagenes(self.lista_imagenes)  
        print('Se encontraron: {0} imágenes.'.format(len(self.lista_imagenes)))  
        respuesta = self.__menu_ordenamiento__()  
        respuesta2 = self.__menu_forma_ord__()  

        respuesta2 = False if respuesta2 is 1 else True  

        lista_ordenada = ordenador.por_fecha(respuesta2) if respuesta is 1 else ordenador.por_usuario(respuesta2)
        # Guarda la lista ya ordenada

        nombre = raw_input('Escribe un nombre para guardar el html: ')  
        Peticiones.copiar_archivos_responsive(nombre)  

        generador = GeneradorHTML(nombre, lista_ordenada)  
        generador.generar_archivo()  

    @staticmethod
    def __menu_forma_ord__():
        Peticiones.limpiar_pantalla()  
        print('\t1. ver de forma ascendente')
        print('\t2. ver de forma descendente')
        return Peticiones.pedir_numero('escribe como deseas visualizar (1 o 2)', 1, 2)  

    @staticmethod
    def __menu_ordenamiento__():
        Peticiones.limpiar_pantalla()  
        cprint('\t\t ¿como deseas que se ordene?  ', 'green', attrs=['bold'])  
        print('\t1. por la fecha')
        print('\t2. por el nombre de usuario')
        return Peticiones.pedir_numero('Escoge una opcion (1 o 2) :  ', 1, 2)  

    @staticmethod
    def __menu_tipo_busqueda__():
        cprint('1. buscar por un hashtag')
        cprint('2. buscar por  popularidad ')
        cprint('3. buscar por coordenadas')

run = Run()
run.menu_busqueda()



