"""
Problema

calcular el promedio de la nota de quices de sus estudiantes para subirla a la plataforma de notas finales
"""

"""
Objetivos Principales

* Recibir el codigo alfanumerico del estudiante
* Calcular el promedio de las notas de quices de los estudiantes.

Subobjetivos
 
* Eliminar la menor nota
* Pasar las notas de 0-100 a 0-5
* Redondear el promedio de las notas finales a dos decimales
* Reportar el promedio ajustado del estudiante
"""

""" 
Pasos para solucionar el problema

1.Definir y almacenar el valor de la nota1
2.Definir y almacenar el valor de la nota2
3.Definir y almacenar el valor de la nota3
4.Definir y almacenar el valor de la nota4
5.Definir y almacenar el valor de la nota5
6.Definir y almacenar el codigo alfanumerico del estudiante
7.Crear y definir una funcion que tome las cinco notas y las pase a valores de 0 a 5
8.Crear y definir una funcion que tome las cinco notas y elimine la menor
9.Crear y difinir una funcion que reciba como parametros las cinco notas del estudiante
    9.1.Esta funcion debera llamr a la funcion de la linea 7 para convertir las notas a valores de 0 a 5
        9.1.1.Formula = NotaEstudiante * (NotaMaximaCeroACien / NotaMaximaCeroACinco)
    9.2.Esta funcion debera llamar a la funcion de la linea 8 para eliminar la menor nota
    9.3.Esta funcion calculara el promedio de las notas y el resultado lo redondeara a dos decimales
10.Imprimir el promedio ajustado de las notas
"""

def NotaMenor(Nota1 = 0, Nota2 = 0, Nota3 = 0, Nota4 = 0, Nota5 = 0):
    Menor = min( (Nota1, Nota2, Nota3, Nota4, Nota5) )
    return Menor

def ConvertirNotas(Nota1 = 0, Nota2 = 0, Nota3 = 0, Nota4 = 0, Nota5 = 0):
    Nota1 = Nota1 / (100 / 5)
    Nota2 = Nota2 / (100 / 5)
    Nota3 = Nota3 / (100 / 5)
    Nota4 = Nota4 / (100 / 5)
    Nota5 = Nota5 / (100 / 5)
    return Nota1, Nota2, Nota3, Nota4, Nota5

""" Esta funcion lo que hace es

1.Convertir las notas de 0-100 a 0-5
2.calcular la nota mas baja(0-100)
3.Calcular el promedio, redondeando a dos decimales la formula
    3.1.La formula primero calcula la suma de todas las cinco notas convertidas
    3.2.Luego la formula convierte la nota menor de 0-100 a 0-5
    3.3.La formula resta el valor convertido de la nota menor a la suma de todas las notas, para eliminar la menor nota
    3.4.El resultado de lo anterior lo divide entre 4
4.Retorna el promedio final del estudiante
"""

def PromedioNotas(Nota1 = 0, Nota2 = 0, Nota3 = 0, Nota4 = 0, Nota5 = 0):
    NotasConvertidas = ConvertirNotas(Nota1, Nota2, Nota3, Nota4, Nota5)
    NotaMasBaja = NotaMenor(Nota1, Nota2, Nota3, Nota4, Nota5)
    Promedio = round((sum( (NotasConvertidas) ) - (NotaMasBaja / (100 / 5))) / 4, 2)
    return Promedio

Nota1 = 80
Nota2 = 50
Nota3 = 40
Nota4 = 90
Nota5 = 60

CodigoEstudiante = "AA23235"
NotaFinal = PromedioNotas(Nota1, Nota2, Nota3, Nota4, Nota5)

print (f"El promedio ajustado del estudiante {CodigoEstudiante} es: {NotaFinal}")