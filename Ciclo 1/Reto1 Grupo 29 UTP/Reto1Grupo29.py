""" 
-----------------------------------------------------------------------------------------------------------------
Problema

Los profesores del MinTIC desean conocer la cantidad de CDs que necesitan comprar para hacer una copia de seguridad del disco duro de sus computadores. Lo han contratado a usted para que realice un algoritmo que calcule la cantidad de los CDs requeridos y el precio más IVA (19%) de los mismos. A la función debe ingresar el nombre del profesor, la capacidad de almacenamiento del disco duro en GB y el valor unitario del CD. Una vez se
han calculado los valores se debe visualizar los resultados obtenidos.
"""

""" 
-----------------------------------------------------------------------------------------------------------------
Objetivo

Realizar un algoritmo que calcule la cantidad de los CDs requeridos y el precio más IVA (19%) de los mismos. A la función debe ingresar el nombre del profesor, la capacidad de almacenamiento del disco duro en GB y el valor unitario del CD. Una vez se han calculado los valores se debe visualizar los resultados obtenidos.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Pseudocodigo

1.Recibir y almacenar el el nombre del profesor (string)
2.Recibir y almacenar el valor unitario de un CD (int)
3.Recibir y almacenar la capacidad de almacenamiento del disco duro en GB (int)
4.Crear una funcion que reciba el nombre del profesor, el valor unitario del cd y la capacidad del disco duro
    4.1.Convertir la capacidad del disco duro a MB y almacenarlo en una variable
    4.2.Dividir la capacidad del disco duro en MB por la cantidad en MB que acepta un CD (usar math.ceil)
    4.3.Calcular el subtotal de la cantidad de discos a utilizar por el valor unitario del CD
    4.4.Sacar el iva del 19 % del subtotal y sumarlo al valor total
    4.5.retornar "Profesor: {nombreProfesor}"
    4.6.retornar “El número de CD que se requiere es {num_cd} y el valor total de los CD es {valor_cds}”
5.Imprimir los resultados
"""

import math

def CalculoCD(NombreProfesor,CapacidadDiscoDuro, ValorCD):
    ConversionMegasAGigas = CapacidadDiscoDuro * 1024.0
    CantidadCD = math.ceil(ConversionMegasAGigas / 700.0)
    Subtotal = CantidadCD * ValorCD
    Total = 0.19 * Subtotal
    Total += round(Subtotal)

    return f"Profesor {NombreProfesor} el número de CD que se requiere es {CantidadCD} y el valor total de los CD es {Total}"

NombreProfesor = input("Ingrese el nombre del profesor: ")
CapacidadDiscoDuro = int(input("Ingrese la capacidad de almacenamiento del disco duro: "))
ValorCD = int(input("Ingrese el valor unitario de un CD: "))

print(CalculoCD(NombreProfesor,CapacidadDiscoDuro, ValorCD))