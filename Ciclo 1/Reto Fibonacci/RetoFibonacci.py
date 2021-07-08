""" 
-----------------------------------------------------------------------------------------------------------------
Problema

Construir una función que permita generar la secuencia de Fibonacci de acuerdo a n términos y luego convertir cada término de la sucesión a su cubo correspondiente, en otras palabras, elevar cada término de la sucesión al cubo.

Casos de prueba

Cantidad de numeros | Resultado parcial | Resultado con elevacion al cubo

10 | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  | [0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304]

5  | [0, 1, 1, 2, 3] | [0, 1, 1, 8, 27]

8  | [0, 1, 1, 2, 3, 5, 8, 13] | [0, 1, 1, 8, 27, 125, 512, 2197]
"""

"""
Solucion 

1.Pedirle y almacenar la cantidad de numeros que tendra la susesion de fibonacci.

2.Crear y definir una funcion que cree la susesion de fibonacci hasta la cantidad de numeros ingresados por el usuario.

3.Crear y definir una funcion que reciba la lista creada por la anterior funcion y la modifique para que cada elemento quede con su respectivo valor al cubo.

4.Mostrar los resultados.
"""

def recur_fibo(Numero: int):
    num1 = 0
    num2 = 1

    Fibonacci = []

    while len(Fibonacci) < Numero:
        Fibonacci.append(num1)
        Fibonacci.append(num2)
        num1 = num1 + num2
        num2 = num2 + num1

    #if len(Fibonacci) == 6:
        #Fibonacci.pop(-1)
        
    return Fibonacci

def iniciar_aplicacion(Numero:int):
    SusesionFibonacci = list(recur_fibo(Numero))

    for j in range(len(SusesionFibonacci)):
        SusesionFibonacci[j] = SusesionFibonacci[j] ** 3

    return SusesionFibonacci


Numero = int(input("Ingrese la cantidad de numeros que tendra la susesion: "))
print(iniciar_aplicacion(Numero))
