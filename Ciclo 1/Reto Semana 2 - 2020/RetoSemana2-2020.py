"""
-----------------------------------------------------------------------------------------------------------------
Problema

Usted trabaja en una entidad financiera que cuenta con la siguiente información en base a la que realizan la
evaluación de nuevas solicitudes de crédito. Recientemente, su empleador adquirió un modelo basado en árboles de decisión para poder realizar más fácilmente una primera revisión de estas solicitudes.

Escriba una función que reciba como parámetro un diccionario en el cuál las llaves son los nombres de las variables mencionadas anteriormente. Retorne un nuevo diccionario con las llaves “id_prestamo” y “aprobado” dónde esta última tenga como valor una variable booleana representando la salida del árbol de decisión. Es decir, informando si el préstamo debe ser aprobado o no.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Objetivo

Escriba una función que reciba como parámetro un diccionario. Retorne un nuevo diccionario con las llaves “id_prestamo” y “aprobado” dónde esta última tenga como valor una variable booleana representando la salida del árbol de decisión. Es decir, informando si el préstamo debe ser aprobado o no.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Pseudocodigo

1.Crear un diccionario donde se almacene tres nuevos diccionarios, en cada diccionario almacenar la siguiente informacion IdPrestamo, Casado, Dependientes, Educacion, Independiente, IngresoDeudor, IngresoCoDeudor, CantidadPrestamo, PlazoPrestamo, HistoriaCredito, TipoPropiedad, donde estos nombres van a actuar como llaves de el diccionario, y el valor va a ser los datos del usuario.

2.Crear una funcion que convierta la parte de casado a un valor booleano, convierta a la cantidad de personas dependientes a numero entero, convierta la educacion en un valor booleano, Convierta independiente en un valor booleano, convierta el tipo de propiedad en un numero si el es urbana sera 1, si es rural sera 2 y si es semiurbana sera 3, Esta funcion debera retornar en forma de variables los datos ya convertidos, esta funcion recibira como parametro el diccionario InfomacionPrestamos y la variable Prestamo.

3.Crear una funcion que reciba como parametro el diccionario con la informacion del prestamo y la variable Prestamo, esta funcion se encargara de evaluar mediante el modelo que contrato el jefe, si el prestamo debe ser o no aprobado.

4.Dentro de la funcion principal llamar a la funcion de ConversionDeTipos(), esta funcion recibira como parametro el diccionario principal y la variable Prestamo.

5.Crear el diccionario que retornara la funcion principal y definir la aprobacion del diccionario como false, dependiendo la condicion que se cumpla en el arbol de desicion, la aprobacion seguira siendo falsa o true.

6.Evaluar dentro de la funcion: 

Si historia credito es igual a 1 entonces
    Si (ingreso codeudor es menor a 0) Y (ingreso deudor divido entre 9 es mayor a la cantidad prestamo)
        AprobacionPrestamos["Aprobado"] = True
    SiNo
        Si (Dependientes es mayor a 2) Y (Independiente es igual a "Si")
            Si (Ingreso Codeudor dividido entre 12) es menor (cantidad prestamo)
                AprobacionPrestamos["Aprobado"] = True
            SiNo
                Si (cantidad prestamo) es menor a (200)
                    AprobacionPrestamos["Aprobado"] = True
SiNo
    Si (independiente es igual a "Si")
        Si Negacion( (Casado) Y (dependientes es mayor a 1) )
            Si (ingreso deudor dividido entre 10 es mayor a cantidad prestamo) O (ingreso codeudor dividido entre 10 es mayor a cantidad prestamo)
                Si (cantidad prestamo es menor a 180)
                     AprobacionPrestamos["Aprobado"] = True
    SiNO
        Si Negacion(el tipo de propiedad es semiurbano) Y (el numero de dependientes es menor a 2)
            Si (Educacion == Graduado)
                Si (ingreso deudor dividido entre 11 es menor a cantidad prestamo) Y (ingreso codeudor dividido entre 11 es menor a cantidad prestamo)
                     AprobacionPrestamos["Aprobado"] = True
                    
7.Retornar el contenido del diccionario de AprobacionPrestamos

8.Almacenar en cada variable la key de cada prestamo, presente en el diccionario InfomacionPrestamos y llamar a la funcion e imprimir el resultado de los tres prestamos.
            
"""

"""
-----------------------------------------------------------------------------------------------------------------
Traduccion
"""

def Prestamo(InfomacionPrestamos,Prestamo) -> dict:
    Casado, Dependientes, Educacion, Independiente, TipoDePropiedad = ConversionDeTipos(InfomacionPrestamos, Prestamo)
    
    AprobacionPrestamos = {
        "CodigoPrestamo": InfomacionPrestamos[Prestamo]["IdPrestamo"],
        "Aprobado": False
    }

    HistoriaCredito = InfomacionPrestamos[Prestamo]["HistoriaCredito"]
    IngresoCoDeudor = InfomacionPrestamos[Prestamo]["IngresoCoDeudor"]
    IngresoDeudor = InfomacionPrestamos[Prestamo]["IngresoDeudor"]
    CantidadPrestamo = InfomacionPrestamos[Prestamo]["CantidadPrestamo"]


    if HistoriaCredito == 1:
        if (IngresoCoDeudor < 0) and ( (IngresoDeudor / 9) > CantidadPrestamo):
            AprobacionPrestamos["Aprobado"] = True
        else:
            if (Dependientes > 2) and (Independiente):
                if (IngresoCoDeudor / 12) < (CantidadPrestamo):
                    AprobacionPrestamos["Aprobado"] = True
            else:
                if (CantidadPrestamo) < (200):
                    AprobacionPrestamos["Aprobado"] = True
    else:
        if (Independiente):
            if not( (Casado) and (Dependientes > 1) ):
                if (IngresoDeudor / 10 > CantidadPrestamo) or (IngresoCoDeudor / 10 > CantidadPrestamo):
                    if (CantidadPrestamo < 180):
                        AprobacionPrestamos["Aprobado"] = True
        else:
            if not( (TipoDePropiedad == 3) and (Dependientes < 2) ):
                if (Educacion):
                    if (IngresoDeudor / 11 < CantidadPrestamo) and (IngresoCoDeudor / 11 < CantidadPrestamo):
                        AprobacionPrestamos["Aprobado"] = True

    return f"{AprobacionPrestamos}"

def ConversionDeTipos(InfomacionPrestamos, Prestamo):
    Casado = InformacionPrestamos[Prestamo]["Casado"] == "Si"
    Dependientes = InformacionPrestamos[Prestamo]["Dependientes"]
    Educacion = InformacionPrestamos[Prestamo]["Educacion"] == "Graduado"
    Independiente = InformacionPrestamos[Prestamo]["Independiente"] == "Si"
    TipoDePropiedad = InformacionPrestamos[Prestamo]["Tipo Propiedad"]
    
    if isinstance(Dependientes, str):
        Dependientes = int(Dependientes[0])

    if TipoDePropiedad == "Urbano":
        TipoDePropiedad = 1
    elif TipoDePropiedad == "Rural":
        TipoDePropiedad = 2
    elif TipoDePropiedad == "Semiurbano":
        TipoDePropiedad = 3

    return Casado, Dependientes, Educacion, Independiente, TipoDePropiedad

InformacionPrestamos = {
        "Prestamo1": {
            "IdPrestamo": "RETOS2_001",
            "Casado": "No",
            "Dependientes": 1,
            "Educacion": "Graduado",
            "Independiente": "Si",
            "IngresoDeudor": 4692,
            "IngresoCoDeudor": 0,
            "CantidadPrestamo": 106,
            "PlazoPrestamo": 306,
            "HistoriaCredito": 1,
            "Tipo Propiedad": "Rural"
        },

        "Prestamo2": {
            "IdPrestamo": "RETOS2_002",
            "Casado": "No",
            "Dependientes": "3+",
            "Educacion": "No graduado",
            "Independiente": "No",
            "IngresoDeudor": 1830,
            "IngresoCoDeudor": 0,
            "CantidadPrestamo": 100,
            "PlazoPrestamo": 306,
            "HistoriaCredito": 0,
            "Tipo Propiedad": "Urbano"
        },

        "Prestamo3": {
            "IdPrestamo": "RETOS2_003",
            "Casado": "No",
            "Dependientes": 0,
            "Educacion": "No graduado",
            "Independiente": "No",
            "IngresoDeudor": 3748,
            "IngresoCoDeudor": 1668,
            "CantidadPrestamo": 110,
            "PlazoPrestamo": 306,
            "HistoriaCredito": 1,
            "Tipo Propiedad": "Semiurbano"
        }
}

Prestamo1 = "Prestamo1"
Prestamo2 = "Prestamo2"
Prestamo3 = "Prestamo3"

print(Prestamo(InformacionPrestamos, Prestamo1))
print(Prestamo(InformacionPrestamos, Prestamo2))
print(Prestamo(InformacionPrestamos, Prestamo3))