"""
-----------------------------------------------------------------------------------------------------------------
Problema

Un profesor desea saber las notas de los estudiantes según las materias que han sido asignadas, teniendo en cuenta que cada una de estas tiene una malla de calificación diferente, la cual es la siguiente:

    * MATEMATICA: 2 Quices 50% - 1 Parcial 50%.
    * FISICA: 3 Quices 45% - 1 Parcial 55%.
    * QUIMICA: 2 Trabajos 30% - 2 Quices 20% - 1 Parcial 50%.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Objetivo

Escriba una función qué reciba cómo parámetro: una variable de tipo diccionario con el nombre del estudiante, la materia con sus respectivas notas de trabajos, quices y parcial, además calcular la nota final y mostrar un mensaje con la siguiente estructura: 
    
    “El estudiante {nombre} obtuvo las siguientes notas: matemáticas: {nota}, física {nota}, química {nota}” .
"""

"""
-----------------------------------------------------------------------------------------------------------------
Pseudocodigo

1.Crear un diccionario, el cual pida y almacene lo siguiente:  
    
    {
        "Nombre": "Ricardo", # Nombre del estudiante
        "MQuiz1": 75, # Nota del primer quiz matemática (0 – 100)
        "MQuiz2": 60, # Nota del segundo quiz matemática (0 – 100)
        "MParc1": 80, # Nota del primer parcial matemática (0 – 100)
        "FQuiz1": 75, # Nota del primer quiz física (0 – 100)
        "FQuiz2": 60, # Nota del segundo quiz física (0 – 100)
        "FQuiz3": 60, # Nota del tercer quiz física (0 – 100)
        "FParc1": 80, # Nota del primer parcial física (0 – 100)
        "QTrab1": 75, # Nota del primer trabajo Química (0 – 100)
        "QTrab2": 60, # Nota del segundo trabajo Química (0 – 100)
        "QQuiz1": 60, # Nota del primer quiz Quimica (0 – 100)
        "QQuiz2": 80, # Nota del segundo quiz Quimica (0 – 100)
        "QParc1": 50 # Nota del primer parcial Quimica (0 – 100)
    }

2.Crear una funcion llamada CalcularNotas(), que reciba como parametro el diccionario que creamos anteriormente

    2.1.Llamar a la funcion que calcula y almacena la nota final del estudiante en la clase de matematicas

        2.1.1.sumar y almacenar las dos notas de los quices.
        2.1.2.al total de la suma de la nota de los quices, dividirlo entre la cantidad de quices.
        2.1.3.el resultado del anterior punto se debe multiplicar por el valor de porcentaje en este caso 0.50.
        2.1.4.tomar el valor del parcial y multiplicarlo por el valor de porcentaje en este caso 0.50.
        2.1.5.las multiplicaciones anteriores deberemos sumarlas y de ahi saldra la nota final de matematicas.

    2.2.Llamar a la funcion que calcula y almacena la nota final del estudiante en la clase de fisica

        2.2.1.sumar y almacenar las tres notas de los quices.
        2.2.2.al total de la suma de la nota de los quices, dividirlo entre la cantidad de quices.
        2.2.3.el resultado del anterior punto se debe multiplicar por el valor de porcentaje en este caso 0.45.
        2.2.4.tomar el valor del parcial y multiplicarlo por el valor de porcentaje en este caso 0.55.
        2.2.5.las multiplicaciones anteriores deberemos sumarlas y de ahi saldra la nota final de fisica.

    2.3.Llamar a la funcion que calcula y almacena la nota final del estudiante en la clase de quimica

        2.3.1.sumar y almacenar las dos notas de los trabajos.
        2.3.2.al total de la suma de la nota de los trabajos, dividirlo entre entre la cantidad de trabajos.
        2.3.3.el resultado del anterior punto se debe multiplicar por el valor de porcentaje en este caso 0.30.
        2.3.4.sumar y almacenar las dos notas de los quices.
        2.3.5.al total de la suma de la nota de los quices, dividirlo entre la cantidad de quices.
        2.3.6.el resultado del anterior punto se debe multiplicar por el valor de porcentaje en este caso 0.20.
        2.3.7.tomar el valor del parcial y multiplicarlo por el valor de porcentaje en este caso 0.50.
        2.3.8.las multiplicaciones anteriores deberemos sumarlas y de ahi saldra la nota final de quimica.
    3.Retornar f"El estudiante {nombre} obtuvo las siguientes notas: matemáticas: {nota}, física {nota}, química {nota}."

3.Imprimir y llamar la funcion.

"""

"""
-----------------------------------------------------------------------------------------------------------------
Traduccion a Python
"""

def CalcularNotas(DiccionarioNotas):
    NotaFinalMatematicas = CalcularNotaMatematicas(DiccionarioNotas)
    NotaFinalFisica = CalcularNotasFisica(DiccionarioNotas)
    NotaFinalQuimica = CalcularNotasQuimica(DiccionarioNotas)
    NombreEstudiante = DiccionarioNotas["Nombre"]

    return f"\n El estudiante {NombreEstudiante} obtuvo las siguientes notas: matemáticas: {NotaFinalMatematicas}, física {NotaFinalFisica}, química {NotaFinalQuimica}."

def CalcularNotaMatematicas(DiccionarioNotas):
    NotaQuices = sum( (DiccionarioNotas["MQuiz1"], DiccionarioNotas["MQuiz2"]) ) / 2
    NotaQuices *= 0.50
    NotaParcial = DiccionarioNotas["MParc1"] * 0.50

    return  NotaQuices + NotaParcial

def CalcularNotasFisica(DiccionarioNotas):
    NotaQuices = sum( (DiccionarioNotas["FQuiz1"], DiccionarioNotas["FQuiz2"], DiccionarioNotas["FQuiz3"]) ) / 3
    NotaQuices *= 0.45
    NotaParcial = DiccionarioNotas["FParc1"] * 0.55

    return  NotaQuices + NotaParcial

def CalcularNotasQuimica(DiccionarioNotas):
    NotaTrabajos = sum( (DiccionarioNotas["QTrab1"], DiccionarioNotas["QTrab2"] ) ) / 2
    NotaTrabajos *= 0.30
    NotaQuices = sum( (DiccionarioNotas["QQuiz1"], DiccionarioNotas["QQuiz2"]) ) / 2
    NotaQuices *= 0.20
    NotaParcial = DiccionarioNotas["QParc1"] * 0.50

    return  NotaQuices + NotaParcial + NotaTrabajos

DiccionarioNotas = {
        "Nombre": input("Ingrese el nombre del estudiante: "),
        "MQuiz1": int(input("Ingrese la nota del primer quiz de matematicas: ")),
        "MQuiz2": int(input("Ingrese la nota del segundo quiz de matematicas: ")),
        "MParc1": int(input("Ingrese la nota del primer parcial de matematicas: ")),
        "FQuiz1": int(input("Ingrese la nota del primer quiz de fisica: ")),
        "FQuiz2": int(input("Ingrese la nota del segundo quiz de fisica: ")),
        "FQuiz3": int(input("Ingrese la nota del tercer quiz de fisica: ")),
        "FParc1": int(input("Ingrese la nota del primer parcial de fisica: ")),
        "QTrab1": int(input("Ingrese la nota del primer trabajo de quimica: ")),
        "QTrab2": int(input("Ingrese la nota del segundo trabajo de quimica: ")),
        "QQuiz1": int(input("Ingrese la nota del primer quiz de quimica: ")),
        "QQuiz2": int(input("Ingrese la nota del segundo quiz de quimica: ")),
        "QParc1": int(input("Ingrese la nota del primer parcial de quimica: "))
}

print(CalcularNotas(DiccionarioNotas))