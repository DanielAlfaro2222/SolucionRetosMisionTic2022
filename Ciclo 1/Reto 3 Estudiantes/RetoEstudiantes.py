"""
-----------------------------------------------------------------------------------------------------------------
Problema

Construya un algoritmo, el cual dado un diccionario que representa la información de los estudiantes y la lista de notas de cada estudiante. Determine cuál de los alumnos de esta lista tiene el promedio más alto y cual tiene el promedio más bajo.

* En caso de que dos o más alumnos tengan el mismo promedio, el mejor promedio
será el del ultimo alumno evaluado dentro del empate.

* La solución debe permitir que se puedan evaluar múltiples entradas, lo cual implica que el diccionario puede tener N cantidad de datos, es decir, N cantidad de estudiantes con sus notas y N cantidad de notas por cada estudiante.

* Las notas están dadas en una lista la cual está contenida dentro del diccionario que ingresa por parámetro, el nombre de la lista es “notas”.

* En caso de empate, se tomará como mejor y peor, el ultimo estudiante evaluado en la lista.

* En caso de que el diccionario no tenga un formato adecuado se deberá regresar un mensaje que diga: “El formato del diccionario no es válido”.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Solucion

1.Crear una funcion que calcule y retorne cual es el estudiante con mayor y menor promedio de notas, esta funcion recibira como parametro un diccionario con la informacion de los estudiantes.

2.Recorrer el diccionario y a cada elemento agregarle el promdio de las notas, ademas eliminar las notas del estudiante, una vez que ya se agrego el promedio de las notas.

3.Recorrer el diccionario y sacar la informacion del estudiante que tenga la nota mas alta y la nota mas baja.
"""

def dar_mejor_peor_estudiante(estudiantes:dict)->str:

    #Recorrer cada elemento del diccionario, sacar y agregar el promedio y eliminaar las notas
    for i in range(len(estudiantes)):
        estudiantes[i]['Promedio'] = round( sum(estudiantes[i]['notas']) / len(estudiantes[i]['notas']), 2) 
        estudiantes[i].pop('notas')

    #Estamos suponiendo que la nota mas alta y la mas baja es la del primer estudiante, luego recorreremos la lista completa de estudiantes revisando y comparando cual es la menor y mayor nota del diccionario y sacaremos la posicion o la key del estudiante.

    NotaMayor = [[len(estudiantes) - 1, estudiantes[len(estudiantes) - 1]['Promedio']]]
    NotaMenor = [[len(estudiantes) - 1, estudiantes[len(estudiantes) - 1]['Promedio']]]

    #Sacar la nota mayor
    for j in range(len(estudiantes)):
        if estudiantes[j]['Promedio'] >= NotaMayor[-1][-1]:
            NotaMayor[0] = [j, estudiantes[j]['Promedio']]

    #Sacar la menor nota
    for x in range(len(estudiantes)):
        if estudiantes[x]['Promedio'] <= NotaMenor[-1][-1]:
            NotaMenor[0] = [x, estudiantes[x]['Promedio']]

    return f"El mejor estudiante es {estudiantes[NotaMayor[0][0]]['name']} con {NotaMayor[0][-1]}\nEl peor estudiante es {estudiantes[NotaMenor[0][0]]['name']} con {NotaMenor[0][-1]}"


"""
-----------------------------------------------------------------------------------------------------------------
Casos de prueba
"""
""" print(dar_mejor_peor_estudiante({ 
                                  0: {'name':'Juan','notas':[3.1,4.2,4,3.9,3.2]},
                                  1: {'name':'Ana', 'notas':[4.1,4.7,4.1,4.9,4.2]}
})) """

""" print(dar_mejor_peor_estudiante({ 
                                  0: {'name':'Juan','notas':[3.1,4.2,4,3.9,3.2]},
                                  1: {'name':'Ana', 'notas':[4.1,4.7,4.1,4.9,4.2]},
                                  2: {'name':'Daniel', 'notas':[4.1,4.7,4.1,4.9,4.2]}
})) """

print(dar_mejor_peor_estudiante({ 
                                  0: {'name':'Juan','notas':[4.1,4.7,4.1,4.9,4.2]},
                                  1: {'name':'Ana', 'notas':[4.1,4.7,4.1,4.9,4.2]},
                                  2: {'name':'Daniel', 'notas':[4.1,4.7,4.1,4.9,4.2]}
}))

""" print(dar_mejor_peor_estudiante({
                                  0: {'name':'Juan', 'notas':[3.1,4.2,4,3.9,3.2]},
                                  1: {'name':'Ana', 'notas':[4.1,4.1,4.1,4.9,4.2]},
                                  2: {'name':'Pedro', 'notas':[4,3.7,4,4,4.2]},
                                  3: {'name':'Pablo', 'notas':[3,3.3,3.4,3.2,3.2]},
                                  4: {'name':'Carlos', 'notas':[4.4,4.8,4.2,4,4.1]}
})) """

""" print(dar_mejor_peor_estudiante({
                                 0: {'name':'Juan', 'notas':[3.1,4.2,4,3.9,3.2]},
                                 1: {'name':'Ana', 'notas':[4.1,4.7,4.1,4.9,4.2]},
                                 2: {'name':'Pedro', 'notas':[4,3.7,4,4,4.2]},
                                 3: {'name':'Pedro', 'notas':[3,3.3,3.4,3.2,3.2]},
                                 4: {'name':'Carlos', 'notas':[3.4,3.8,4.2,4,4.1]},
                                 5: {'name':'Maria', 'notas':[4.4,4.7,4.6,4.1,4.2]},
                                 6: {'name':'Luisa','notas':[4.8,4.7,4.5,4.5,4.9]}
})) """