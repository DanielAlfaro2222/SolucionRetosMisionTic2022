""" 3023433299 """

""" 
-----------------------------------------------------------------------------------------------------------------
Problema

Se desea entonces construir una función la cual a partir de los valores a, b, y c de la ecuación de la parábola, calcule los puntos de interés mencionados (puntos de corte con X, punto de corte con Y, coordenadas del vértice y la evaluación de la función en 4 puntos determinados).Dicha función debe anidar cuatro funciones más que calcularan por separado los valores de interés.
"""

""" 
-----------------------------------------------------------------------------------------------------------------
Objetivo

Construir una función la cual a partir de los valores a, b, y c de la ecuación de la parábola, calcule los puntos de interés mencionados (puntos de corte con X, punto de corte con Y, coordenadas del vértice y la evaluación de la función en 4 puntos determinados)
"""

""" 
-----------------------------------------------------------------------------------------------------------------
Informacion sobre el problema

1.Formula canonica de toda parabola es:

    f(x) = (a * (x ** 2)) + b * x + c

2.Los valores de a, b y c, son valores que se pueden pedir al usuario, los valores de X1, X2, X3, X4, son valores constantes, los cuales equivalen a esto:

   | X1 = -1 | X2 = 4 | X3 = 1 | X4 = -1 |

3. Calcular los puntos de corte del eje X, primero se calcula el eje X1, luego X2, con la siguiente formula:

    x1 = (-b +  (((b ** 2) - (4 * a * c)) ** (1/2))) / 2 * a
    x2 = (-b -  (((b ** 2) - (4 * a * c)) ** (1/2))) / 2 * a

4.El punto de corte del eje y, es igual al valor de la variable C.

5. Calcular la punto X, en el vertice con la siguiente formula:

    x = -b / (2 * a)

6.

"""




