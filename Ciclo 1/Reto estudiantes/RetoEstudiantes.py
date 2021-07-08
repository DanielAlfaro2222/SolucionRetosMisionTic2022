from functools import reduce


def buscar_estudiantes(notas: dict):

    try:
        nota = float(input("Ingrese una nota: "))
    except:
        return f"\nError en el dato ingresado"

    Lista = list(reduce(lambda notas=list(), x=dict()
                 : notas + x, notas.items()))

    # Crear una sola lista compuesta con los datos de cada estudiante
    ListaFinal = list(filter(lambda x: isinstance(x, dict), Lista))

    # Funcion para calcular el promedio de la nota de cada estudiante
    def SacarPromedioNotas(estudiante: dict):
        estudiante['notas'] = round(sum(estudiante['notas']) / 5, 1)
        return estudiante

    PromedioNotas = list(map(SacarPromedioNotas, ListaFinal))

    ListadoEstudiantesPromedioBajo = list(
        filter(lambda x: x['notas'] < nota, PromedioNotas))

    return ListadoEstudiantesPromedioBajo


students = {'a': {'name': 'Juan', 'notas': [3.1, 2.2, 2.5, 3.9, 3.2]},
            'j': {'name': 'Jenny', 'notas': [2, 3.7, 2, 2, 2.2]},
            'c': {'name': 'Ana', 'notas': [2.6, 2.7, 2.1, 2.9, 2.2]},
            'y': {'name': 'Pedro', 'notas': [2, 3.5, 2, 2, 2.2]},
            'x': {'name': 'Pablo', 'notas': [2, 3.3, 3.9, 3.2, 3.2]},
            'l': {'name': 'Carlos', 'notas': [3.2, 3.8, 2.2, 2, 2.1]},
            'v': {'name': 'Maria', 'notas': [2.8, 2.7, 2.8, 2.9, 2.8]},
            'r': {'name': 'Luisa', 'notas': [2.8, 2.7, 3.5, 2.5, 2.9]},
            'b': {'name': 'Mario', 'notas': [2.2, 3.2, 3, 3.2, 2.2]},
            'g': {'name': 'Fabio', 'notas': [2.4, 3.2, 3.1, 3.2, 2.2]}
            }

print(buscar_estudiantes(students))
