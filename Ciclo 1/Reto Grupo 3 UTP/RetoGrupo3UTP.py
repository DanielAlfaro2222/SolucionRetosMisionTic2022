"""
-----------------------------------------------------------------------------------------------------------------
Problema

Una empresa desea saber el total a pagar un empleado durante 1 día laborado, teniendo en cuenta que la empresa paga a sus empleados según las horas laborales trabajadas y horas extras las cuales se deben calcular automáticamente si pasan de 8 horas.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Objetivo

Escriba una función qué reciba cómo parámetro: una variable de tipo diccionario con el nombre del trabajador, horas trabajadas, bonificación, que permita calcular el valor a pagar al empleado incluyendo las prestaciones de ley durante un día, es importante redondear a dos decimales el valor total a pagar, además debe mostrar un mensaje con la siguiente estructura: “El empleado {nombre} total a pagar {total}”.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Pseudocodigo

1.Crear un diccionario que almacene los datos del usuario, las horas trabajadas, la bonificacion recibida y el valor de la hora laboral, el valor de la hora extra, el valor del auxilio de transporte y el descuento en salud y pension.

2.Crear una funcion que reciba como parametro el diccionario que se creo en el punto anterior, la cual calcular el total a pagar de un dia laborado.

3.Calcular el valor a pagar de las horas laborales (8 horas).

4.Calcular el valor a pagar por las horas extras (superior a 8 horas).

5.Sumar el total de las horas laborales, el valor de las horas extras, el valor de la bonificacion diaria y el auxilio de transporte mensual.

6.Al total a pagar, restarle el pago por salud y pension mensual.

7.Retornar el total a pagar.
"""

def CalcularPago(Empleado) -> str:
    Nombre = Empleado["Nombre"]
    if Empleado["HorasTrabajadas"] >= 8:
        TotalHorasTrabajas = Empleado["HorasTrabajadas"] * Empleado["ValorHoraLaborada"]
        TotalHorasExtras = (8 - Empleado["HorasTrabajadas"]) * Empleado["ValorHoraExtra"]
    else:
        TotalHorasExtras = 0 
        TotalHorasTrabajas = Empleado["HorasTrabajadas"] * Empleado["ValorHoraLaborada"] 

    TotalAPagar = sum( (TotalHorasTrabajas, TotalHorasExtras, Empleado["AuxilioTransporteMensual"], Empleado["Bonificacion"] ) )

    TotalAPagar = TotalAPagar - Empleado["SaludYPensionMensual"]

    return f"\n El empleado {Nombre} total a pagar {TotalAPagar}"


Empleado = {
    "Nombre": input("Ingrese el nombre de el empleado: "),
    "HorasTrabajadas": int(input("Ingrese el numero de horas trabajadas en el dia: ")),
    "Bonificacion": float(input("Ingrese la cantidad de bonificacion recibida en el dia: ")),
    "ValorHoraLaborada": 3785,
    "ValorHoraExtra": 4731,
    "AuxilioTransporteMensual": 106454 / 31, 
    "SaludYPensionMensual": 258927 / 31
}

print(CalcularPago(Empleado))