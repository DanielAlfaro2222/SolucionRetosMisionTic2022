"""
-----------------------------------------------------------------------------------------------------------------
Problema

En una empresa de logística, cuentan con un sistema de información para la operación y toma de decisiones. Se ha identificado la necesidad de incorporar una funcionalidad a este sistema de información, con el fin de agilizar la distribución de cajas cuadradas frágiles en sus vehículos, sobre las cuales no se puede colocar nada encima. 

Las cajas transportadas por este operador logístico, pueden presentar tamaños que varían mucho, generando bastante desperdicio de espacio si se distribuyen sin ningún criterio, en los pallets y contenedores de los vehículos disponibles.
"""

""" 
-----------------------------------------------------------------------------------------------------------------
Objetivo del problema

Se necesita entonces implementar una función (algoritmo), que reciba el lado de cada una de
estas cajas cuadradas, junto con el porcentaje de ajuste, y determine si se puede realizar el
empacado parcial o total de las piezas, informando el número de piezas aprobadas y el área
acumulada que será ocupada por estas si se realiza. Si no se realiza, informar la cantidad de
piezas que fueron rechazadas. En la siguiente tabla se muestran los ejemplos de las figuras,
cómo deberían ser procesados (entradas y reporte de salida)
"""

"""
-----------------------------------------------------------------------------------------------------------------
Apuntes sobre el problema

1.Formula para hallar el area promedio
    AreaPromedio = (sum( (30 ** 2, 10 ** 2, 20 ** 2, 25 ** 2) ) / 4 ) ** (1/2)

2.Para aprobar el embalaje por lo menos 2 de las cuatro cajas cumplan con el criterio del ajuste.

3.Formula para hallar la diferencia permitida entre el area de una pieza y el area promedio de todas las cajas.
    DiferenciaPermitida = PorcentajeAjuste ∗ AreaPromedio

4.Para hallar la diferencia entre el area de la pieza y el area promedio, usaremos esta formula, esto para saber si la pieza es confirmada o rechazada.
    abs(AreaPromedio − AreaPieza)
"""

"""
-----------------------------------------------------------------------------------------------------------------
Pseudocodigo para solucionar el problema

1.Definir y almacenar el lado de la pieza 1
2.Definir y almacenar el lado de la pieza 2
3.Definir y almacenar el lado de la pieza 3
4.Definir y almacenar el lado de la pieza 4
5.Hallar y almacenar el area de la pieza 1 usando la formula => lado1 ** 2
5.Hallar y almacenar el area de la pieza 2 usando la formula => lado2 ** 2
6.Hallar y almacenar el area de la pieza 3 usando la formula => lado3 ** 2
7.Hallar y almacenar el area de la pieza 4 usando la formula => lado4 ** 2
8.Hallar y almacenar el area promedio de las cuatro piezas usando la formula:
    (sum( (areaLado1, areaLado2, areaLado3, areaLado4)) / 4) ** (1/2)
9.Hallar y almacenar la diferencia permitida entre el area de la pieza y el area promedio, usando la formula: 
    PorcentajeAjuste * AreaPromedio
10.Hallar y almacenar la diferencia entre el area de la pieza y el area promedio, usando la formula:
    abs(AreaPieza - AreaPromedio)
11.Crear una variable contadora e inicializarla en cero, para las piezas que sean permitidas
12.Crear una variable contadora e inicializarla en cero, para las piezas que no sean permitidas
13.Crear una variable acumuladora e inicializarla en cero, para acumular el total del area ocupada por las piezas permitidas
14.Crear una codicion, la cual evaluara si el total de piezas aprobadas es igual o mayor a 2, si esta condicion es verdadera retornar el siguiente mensaje "Embalaje confirmado: piezas aprobadas = 4, superficie ocupada = 3600".
5.Si la condicion no se cumple, mostrar el siguiente mensaje "Embalaje descartado 3 piezas no ajustan"
"""

"""Traduccion al lenguaje de programacion"""

def empaquetador(PorcentajeAjuste, Lado1, Lado2, Lado3, Lado4):
    AreaPieza1 = Lado1 ** 2
    AreaPieza2 = Lado2 ** 2
    AreaPieza3 = Lado3 ** 2
    AreaPieza4 = Lado4 ** 2


    AreaPromedio = (sum( (AreaPieza1, AreaPieza2, AreaPieza3, AreaPieza4) ) / 4)

    DiferenciaPermitida = PorcentajeAjuste * AreaPromedio

    PiezasPermitidas = 0
    PiezasNoPermitidas = 0
    TotalAreaOcupada = 0

    DiferenciaAreaPieza1 = abs(AreaPieza1 - AreaPromedio)
    if DiferenciaAreaPieza1 <= DiferenciaPermitida:
        PiezasPermitidas += 1
        TotalAreaOcupada += AreaPieza1
    else:
        PiezasNoPermitidas += 1 
    
    DiferenciaAreaPieza2 = abs(AreaPieza2 - AreaPromedio)
    if DiferenciaAreaPieza2 <= DiferenciaPermitida:
        PiezasPermitidas += 1 
        TotalAreaOcupada += AreaPieza2
    else:
        PiezasNoPermitidas += 1 

    DiferenciaAreaPieza3 = abs(AreaPieza3 - AreaPromedio)
    if DiferenciaAreaPieza3 <= DiferenciaPermitida:
        PiezasPermitidas += 1 
        TotalAreaOcupada += AreaPieza3 
    else:
        PiezasNoPermitidas += 1 

    DiferenciaAreaPieza4 = abs(AreaPieza4 - AreaPromedio)
    if DiferenciaAreaPieza4 <= DiferenciaPermitida:
        PiezasPermitidas += 1 
        TotalAreaOcupada += AreaPieza4 
    else:
        PiezasNoPermitidas += 1

    if PiezasPermitidas >= 2:
        return f"Embalaje confirmado: piezas aprobadas = {PiezasPermitidas}, superficie ocupada = {TotalAreaOcupada}"
    else:
        return f"Embalaje descartado {PiezasNoPermitidas} piezas no ajustan"

print(empaquetador(0.2, 30, 30, 30, 30))
print(empaquetador(0.5, 30, 10, 20, 25))
print(empaquetador(0.8, 30, 10, 20, 25))
print(empaquetador(0.8, 30, 10, 5, 30))