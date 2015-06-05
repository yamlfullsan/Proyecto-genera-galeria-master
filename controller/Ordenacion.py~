# coding=utf-8
from operator import itemgetter


class OrdenadorImagenes:
    def __init__(self, lista):
        self.lista = lista  # Crea campo con la lista de los datos de las imágenes

    def por_fecha(self, descenente):
        #  Ordenación por fecha; modo de ordenación: año, mes, día, hora, minutos, segundos
        lista_ordenada = sorted(self.lista, key=itemgetter(6, 5, 4, 7, 8, 9), reverse=descenente)
        return lista_ordenada  # Devuelve la lista ordenada

    def por_usuario(self, descenente):
        # Ordena por orden alfabético los nombre de usuario
        lista_ordenada = sorted(self.lista, key=itemgetter(1), reverse=descenente)
        return lista_ordenada  # Devuelve la lista ordenada
