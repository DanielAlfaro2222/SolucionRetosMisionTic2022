"""
----------------------------------------------------------------------------------------------------------------
construya un sistema para determinar la cantidad a instalar de nuevas antenas para la transmisión de información en zonas rurales o de difícil acceso, en pos del mejoramiento de la calidad de vida de los ciudadanos
"""

"""
----------------------------------------------------------------------------------------------------------------
Objetivo => Para ello, el sistema debe recibir como entrada el área de la zona en la que se desean
instalar las nuevas antenas en metros cuadrados, así como la cantidad de antenas previamente
instaladas y el tipo de las nuevas antenas. Las antenas previamente instaladas tienen
un rango de alcance de 16600 metros y las nuevas antenas a instalar tienen un rango de
50600 m , 19200 m , 36900 m , 40500 m y 34200 m para los tipos “a”, “b”, “c”, “d” y “e”
respectivamente.

Finalmente se debe mostrar por pantalla, la cantidad de nuevas antenas necesarias
para instalar. Si esta cantidad es negativa, se debe mostrar el valor 0.

Además, la cantidad de antenas previamente instaladas tiene que ser un número entero
mayor o igual a 0 y el tipo de las nuevas antenas tiene que estar entre los antes
mencionados, en caso contrario, mostrar por pantalla el mensaje “error en los datos”.
"""

""" 
----------------------------------------------------------------------------------------------------------------
Pasos para solucionar el problema

1.Recibir y almacenar el area de la zona en la que se va a instalar las nuevas antenas en metros cuadrados.
2.Recibir y almacenar la cantidad de antenas previamente instaladas.
    2.1.La cantidad de antenas debe ser mayor o igual a 0, sino mostrar error.
3.Recibir y almacenar el tipo de las nuevas antenas.
    3.1.Las antenas previamente instaladas tienen un rango de alcance de 16600 metros.
    3.2.Las nuevas antenas a instalar tienen un rango de:
        a = 50600 metros
        b = 19200 metros
        c = 36900 metros
        d = 40500 metros
        e = 34200 metros
4.Crear una funcion que calcule la cantidad de nuevas antenas necesarias para instalar
    4.1.Si la cantidad es negativa retornar un 0.
5.Mostrar resultados.
"""

# Esta funcion calcula el numero de antenas nuevas necesarias para cubrir la zona




import math
def CalculoAntenasNecesarias(AreaZona=0, AntenasPrevias=0, TipoNAntenas="0"):

    Diferencia = AreaZona - (16600 * AntenasPrevias)

    if TipoNAntenas == 'a':
        Resultado = math.ceil(Diferencia / 50600)
    elif TipoNAntenas == 'b':
        Resultado = math.ceil(Diferencia / 19200)
    elif TipoNAntenas == 'c':
        Resultado = math.ceil(Diferencia / 36900)
    elif TipoNAntenas == 'd':
        Resultado = math.ceil(Diferencia / 40500)
    elif TipoNAntenas == 'e':
        Resultado = math.ceil(Diferencia / 34200)

    return Resultado


DatosValidos = True
AreaZona = float(input(
    "Ingrese el area de la zona, a la cual se le van a instalar las nuevas antenas: "))
if AreaZona < 0 or AreaZona == 0:
    DatosValidos = False

AntenasPrevias = int(
    input("Ingrese la cantidad de antenas previamente instaladas: "))

if AntenasPrevias < 0:
    DatosValidos = False

TipoNAntenas = input("Ingrese el tipo de las nuevas antenas: ").lower()

if TipoNAntenas not in ('a', 'b', 'c', 'd', 'e'):
    DatosValidos = False

if DatosValidos == False:
    print("\n Error en los datos")
else:
    print(CalculoAntenasNecesarias(AreaZona, AntenasPrevias, TipoNAntenas))
