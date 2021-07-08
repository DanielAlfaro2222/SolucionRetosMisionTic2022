"""
-----------------------------------------------------------------------------------------------------------------
Problema

Se requiere una función que procese la información que contiene el diccionario proveniente de la base de datos, y retorne:

1) El número de consignaciones en los cajeros que están fallando (Fuera de Servicio y Cerrados).

2) Recaudo total de las consignaciones realizadas en los cajeros del numeral (1), con el fin de realizar una proyección del dinero que podría dejar de recaudarse al tener estos equipos sin operar.

3) Listado de modelos (sin repeticiones y en orden ascendente) de los equipos que no están operando.
"""

import pprint as pp
from typing import List
from casosGeneradosP45 import *


def recaudoModelosDefectuosos(caso):

    from functools import reduce
    # ---------Filtar la informacion de todos los cajeros que no estan operando-------------

    def PredicadoInformacionCajerosNoOperativos(caso):
        return caso['estado'] == 'Fuera de Servicio' or caso['estado'] == 'Cerrado'

    ListadoInformacionCajerosNoOperativos = list(
        filter(PredicadoInformacionCajerosNoOperativos, caso.values()))

    # ---------Traernos el listado de todos los cajeros que no estan operando-------------
    ListadoCajerosNoOperativos = set(
        map(lambda x: x['modeloCajero'], ListadoInformacionCajerosNoOperativos))

    ListadoCajerosNoOperativos = sorted(list(ListadoCajerosNoOperativos))

    # ----Traernos todos las transacciones de los cajeros que no estan operando----------

    ListadoTransaccionesCajerosNoOperativos = list(
        map(lambda x: x['transacciones'], ListadoInformacionCajerosNoOperativos))

    ListadoTransaccionesCajerosNoOperativos = list(reduce(lambda contenedor=list(
    ), x=dict(): contenedor + x, ListadoTransaccionesCajerosNoOperativos))

    def PredicadoListadoFiltradoTransacciones(elemento):
        return elemento['tipoMovimiento'] == 'consignacion'

    ListadoFiltradoTransaccionesCajerosNoOperativos = list(filter(
        PredicadoListadoFiltradoTransacciones, ListadoTransaccionesCajerosNoOperativos))

    # ----Sacar el total de los montos de los cajeros que no estan operado----------

    TotalMonto = list(
        map(lambda x: x['monto'], ListadoFiltradoTransaccionesCajerosNoOperativos))

    # return {'numeroConsignaciones': len(ListadoFiltradoTransaccionesCajerosNoOperativos), 'totalRecaudado': sum(TotalMonto), 'listadoModelosFallando': ListadoCajerosNoOperativos}

    return ListadoInformacionCajerosNoOperativos


"""
-----------------------------------------------------------------------------------------------------------------
Casos de prueba

Resultado caso 1

{'numeroConsignaciones': 39, 'totalRecaudado': 12810000,
    'listadoModelosFallando': [100, 101, 2017, 2020]}

Resultado caso 2

{'numeroConsignaciones': 14, 'totalRecaudado': 2780000,
    'listadoModelosFallando': [100, 101, 2020]}

Resultado caso 3

{'numeroConsignaciones': 2, 'totalRecaudado': 1500000,
    'listadoModelosFallando': [100, 2017, 2020]}

Resultado caso 4

{'numeroConsignaciones': 17, 'totalRecaudado': 6920000,
    'listadoModelosFallando': [100, 2017, 2020]}
"""

pp.pprint(recaudoModelosDefectuosos(caso1))
# print(recaudoModelosDefectuosos(caso2))
# print(recaudoModelosDefectuosos(caso3))
# print(recaudoModelosDefectuosos(caso4))
