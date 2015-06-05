# coding=utf-8


class GeneradorHTML:
    def __init__(self, nombre_de_archivo, datos):
        self.name_index =  nombre_de_archivo + '/' + 'index.html'  
        self.datos = datos  

    def generar_archivo(self):
        archivo_html = open(self.name_index, 'w')  
        with open('model/Skeleton/html', 'r') as file_codigo:  
            for linea in file_codigo:
                if '<!--aqui-->' in linea:  
                    for elemento in self.datos: 
                        row = self.__crear_row__(elemento)  
                        archivo_html.write(row)  
                else:
                    archivo_html.write(linea)  
        archivo_html.close()  

    def pasar_datos_dic(self, datos_tupla):
        datos = {'url': datos_tupla[0],  
               'usuario': datos_tupla[1],  
               'fecha': '{0}/{1}/{2}'.format(self.formato_numero(datos_tupla[4]),  
                                             self.formato_numero(datos_tupla[5]),  
                                             datos_tupla[6]),  
               'descripcion': datos_tupla[2],  
               'tags': datos_tupla[3],  
               'hora': '{0}:{1}:{2}'.format(self.formato_numero(datos_tupla[7]),  
                                            self.formato_numero(datos_tupla[8]),  
                                            self.formato_numero(datos_tupla[9])), 
               'link': datos_tupla[10]}  
        return datos  

    @staticmethod
    def formato_numero(numero):
        if numero <= 9:
            return '0{0}'.format(numero)
        else:
            return str(numero)

    def __crear_row__(self, datos_tupla):
        datos = self.pasar_datos_dic(datos_tupla)
        row = '\t<div class="row">\n' \
                    '\t\t<div class="col-lg-3 col-md-4 col-sm-6 col-xs-12">\n' \
                        '\t\t\t<a class="thumbnail" href="http://{0}">\n'\
                            '\t\t\t\t<img class="img-responsive" src="{1}" alt="">\n'\
                        '\t\t\t</a>\n' \
                    '\t\t</div>\n' \
                    '\t\t<div class="col-lg-9 col-md-8 col-sm-6 col-xs-6">\n' \
                        '\t\t\t<br><li>\n' \
                            '\t\t\t\t<ul><b>{2}</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{3} {4}</ul>\n' \
                            '\t\t\t\t<ul class="informacion">{5}</ul>\n' \
                            '\t\t\t\t<ul class="informacion">{6}</ul>\n' \
                        '\t\t\t</li>\n' \
                    '\t\t</div>\n' \
                '\t</div>\n'.format(datos['link'], datos['url'], datos['usuario'], datos['fecha'], datos['hora'],
                                    datos['descripcion'], datos['tags'])
        return row  
