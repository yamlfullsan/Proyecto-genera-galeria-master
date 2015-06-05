# coding=utf-8
from operator import itemgetter


class OrdenadorImagenes:
    def __init__(self, lista):
        self.lista = lista 

    def por_fecha(self, descenente):
        
        lista_ordenada = sorted(self.lista, key=itemgetter(6, 5, 4, 7, 8, 9), reverse=descenente)
        return lista_ordenada  

    def por_usuario(self, descenente):
       
        lista_ordenada = sorted(self.lista, key=itemgetter(1), reverse=descenente)
        return lista_ordenada  
