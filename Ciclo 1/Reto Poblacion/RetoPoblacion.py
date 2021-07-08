""" 
----------------------------------------------------------------------------------------------------------------
Problema

Escriba una función que permita llevar a cabo el estudio y que reciba cómo parámetros: una tupla correspondiente a la población X y la población Y. Así mismo deberá recibir el número de veces a ejecutar el estudio. La función deberá dar como resultado un diccionario con la cantidad de años que tomó en cada caso que la cantidad de ciudadanos de la población X fuera mayor a la cantidad de ciudadanos de la población Y así como las poblaciones X, Y finales en cada ejecución del estudio o corrida.

Para la realización del estudio comparativo se establecen las siguientes premisas que deben ser cumplidas:

* Los valores iniciales de la población X y Y deben ser cargados como una tupla, en la cual el primer elemento de la tupla es el valor de población X y el segundo valor de la tupla es el valor de la población Y al iniciar el estudio.

* En el primer año la población X tiene menos ciudadanos que la población Y, si esta condición no se cumple las poblaciones no son aptas para el estudio.

* La tasa de crecimiento de ciudadanos anual de la población X es del 8% y la tasa de crecimiento anual de ciudadanos de la población Y es del 3.5%. (Los aumentos de las poblaciones deberán convertirse a enteros).

* El estudio deberá ser ejecutado una cantidad n de veces indicadas y en cada ejecución se aumentará en un 7% la cantidad de ciudadanos de la población X con respecto al año inmediatamente anterior y en un 18% la cantidad de ciudadanos de la población Y con respecto al año inmediatamente anterior.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Solucion

1.Crear la funcion que realiza el estudio demografico, esta funcion recibira como parametro una tupla(poblacion en X y poblacion en Y) y un numero entero(numero de veces que se realizara el estudio).

2.Crear una variable con el año de inicio.

3.Evaluar si la poblacion en X es menor a la poblacion en Y en el primer año, si esto ocurre se podra iniciar el estudio, sino la funcion debera retornar la polacion no es apta para el caso de estudio.

4.Crear un bucle for en el cual 
"""

def estudioDemografico (poblacion:tuple, n:int)->dict:

    Año = 2017
    ResultadoEstudioDemografico = dict()
    PoblacionX = poblacion[0]
    PoblacionY = poblacion[1]

    if PoblacionX >= PoblacionY:
        return f"Los valores de las poblaciones no son adecuados para el estudio"
    else:
        for i in range(n):
            PoblacionX += int(PoblacionX * 0.15)
            PoblacionY += int(PoblacionY * 0.21)
            if i == 0:
                ResultadoEstudioDemografico.update({f"Año{i + 1}": Año})
                ResultadoEstudioDemografico.update({f"PobX{i + 1}": PoblacionX})
                ResultadoEstudioDemografico.update({f"PobY{i + 1}": PoblacionY})
            else:
                Año += 2
                ResultadoEstudioDemografico.update({f"Año{i + 1}": Año})
                ResultadoEstudioDemografico.update({f"PobX{i + 1}": PoblacionX})
                ResultadoEstudioDemografico.update({f"PobY{i + 1}": PoblacionY})

    return ResultadoEstudioDemografico


"""
-----------------------------------------------------------------------------------------------------------------
Casos de estudio
"""

print(estudioDemografico((1000, 2000), 4))

print(estudioDemografico((9000, 2000), 2))