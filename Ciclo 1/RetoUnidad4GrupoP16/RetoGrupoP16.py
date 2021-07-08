""" -----------------------------------------------------------------------------------------------------------------
Problema

Escriba una función que reciba un diccionario que contiene la información previamente especificada. Retorne una tupla, en la que el primer elemento sea un código generado con las tres primeras letras del nombre seguido de una clave que se obtiene de la siguiente manera; concatenando cada número par de la cédula multiplicado por la sumatoria de los números impares de la misma cédula.

El segundo elemento debe ser el nombre y el último elemento es el promedio de las ventas
anuales redondeado a dos decimales, como se muestra en la siguiente estructura.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Solucion

1.Crear una funcion que se encargue de la creacion del codigo.

2.Recorrer cada elemento del diccionario principal y crear el codigo.
"""
# from CasosDePrueba import *
# def mejor_promedio_anual(datos: dict) -> tuple:
#     pass


# def CrearCodigo(datos: dict):
#     Codigo = ''

#     # for elemento in datos.keys():
#     #     elemento['cedula'].split(',')

#     for elemento in datos.keys():
#         Codigo += datos[elemento]["nombre_emp"][:3]
#         # Pares = list(map(lambda x:, datos[elemento]['cedula']))
#         Pares = list(filter(lambda lista=list(), x=0: lista(int(x % 2 == 0)),
#                      datos[elemento]["cedula"]))
#     return Pares


# print(CrearCodigo(caso))
