""" 
-----------------------------------------------------------------------------------------------------------------
Problema

Metro se caracteriza por tener el conteo de cuantas veces llega un cliente en una semana, por esto ha decidido contratar a un ingeniero de Sistemas e informática para realizar un algoritmo en Python que agrupe las veces que un cliente ha ingresado y mostrar la información de dos formas distintas: una en la que mostrará el total de veces ingresadas en toda la semana y la última mostrará el número de veces seguida que vino en la semana.

Para realizar el ejercicio, se realizarán tres funciones, las cuales son:

* Primera Función: Esta función recibe como parámetro único una lista con los clientes. Esta función debe retornar en una lista la cantidad de veces que se nombra en la lista, esta información se guardará en una tupla en la lista de la siguiente manera: (cliente, Nveces).

* Segunda Función: Esta función recibe como parámetro único una lista con los clientes. Esta función debe retornar en una lista la cantidad de veces seguidas que el cliente ha llegado, esta información se guardará en una tupla en la lista de la siguiente manera: (cliente, Nveces).

* Tercera Función: Esta función recibe como parámetros, una lista generada ya sea por la Primera Función o la Segunda Función, y un número que dará la opción a imprimir, este número es para saber si deseamos imprimir la Primera Función o la Segunda Función. Esta función debe retornar la información de las tuplas de dos maneras:   

        * Primer caso (1), “El cliente {n[0]} aparece {n[1]} vez” o “El cliente {n[0]} aparece {n[1]} veces repetido"”.

        * Segundo caso (2), “El cliente {n[0]} tiene {n[1]} repetición seguida” o “El cliente {n[0]} tiene {n[1]} repeticiones seguidas”. Si el usuario ingresa una opción no valida. Debe retornar el mensaje: “Ingresa un número valido”.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Solucion

1. Definir la primer funcion que recibira una lista con los clientes, luego crear una nueva lista, en la cual se va a ir almacenando cada uno de los clientes y la cantidad de veces que se repiten en forma de tupla.

2.Definir la segunda funcion que recibira una lista con los clientes, luego creara una nueva lista con el numero de veces seguidas que el cliente ingreso a la tienda.

3.Definir la tercer funcion que recibira una lista con los clientes y una opcion, dependiendo de el numero de la opcion, imprimira la funcion 1 o la funcion 2.
"""

def VerCantidadRepetidos(ListaClientes: list)->list:
    
    ConjuntoNombres = list()

    [ConjuntoNombres.append(nombre) for nombre in ListaClientes if nombre not in ConjuntoNombres]

    ClientesRepetidos = list()

    [ClientesRepetidos.append((ConjuntoNombres[i], ListaClientes.count(nombre))) for i,nombre in enumerate(ConjuntoNombres)]

    return ClientesRepetidos

def VerRepetidosEnLaMismaLinea(ListaClientes: list)->list:
    
    ClientesSeguidos = list()

    iterador = 1
    for i in range(1,len(ListaClientes)):
        if ListaClientes[i-1] == ListaClientes[i]:
            iterador += 1
        else:
            if iterador > 1:
                ClientesSeguidos.append((ListaClientes[i - 1], iterador))
                iterador = 1

    return ClientesSeguidos

def ImprimirVectores(ListaClientes: list, Opcion: int)->str:

    PrimerFuncion = VerCantidadRepetidos(ListaClientes)
    SegundaFuncion = VerRepetidosEnLaMismaLinea(ListaClientes)

    try:
        if Opcion == 1:
            for i in range(len(PrimerFuncion)):
                if PrimerFuncion[i][1] != 1:
                    print(f"El cliente {PrimerFuncion[i][0]} aparece {PrimerFuncion[i][1]} veces repetido")
                else:
                    print(f"El cliente {PrimerFuncion[i][0]} aparece {PrimerFuncion[i][1]} vez")
        else:
            for i in range(len(SegundaFuncion)):
                if SegundaFuncion[i][1] != 1:
                    print(f"El cliente {SegundaFuncion[i][0]} tiene {SegundaFuncion[i][1]} repeticiones seguidas")
    except:
        return f"Opcion escogida incorrecta"

"""
-----------------------------------------------------------------------------------------------------------------
Casos de prueba primera funcion
"""
""" print(VerCantidadRepetidos(["Santiago","Santiago","Santiago", "Laura", "Laura", "Laura", "Laura","Pérez"]))

print(VerCantidadRepetidos(["Santiago","Santiago","Santiago", "Laura", "Laura","Laura","Laura","Pérez","Pérez","Pérez","Santiago","Pedro"])) """

"""
-----------------------------------------------------------------------------------------------------------------
Casos de prueba segunda funcion
"""
""" print(VerRepetidosEnLaMismaLinea(["Santiago","Santiago","Santiago", "Laura", "Laura", "Laura","Laura","Pérez"]))

print(VerRepetidosEnLaMismaLinea(["Santiago","Santiago","Santiago", "Laura", "Laura","Laura","Laura","Pérez","Pérez","Pérez","Santiago","Pedro"])) """

"""
-----------------------------------------------------------------------------------------------------------------
Casos de prueba tercera funcion
"""

#Primera opcion
print(ImprimirVectores(["Santiago","Santiago","Santiago","Laura", "Laura", "Laura", "Laura","Pérez"], 1))

print(ImprimirVectores(["Santiago","Santiago","Santiago", "Laura", "Laura","Laura","Laura","Pérez","Pérez","Pérez","Santiago","Pedro"],1))

#Segunda opcion
print(ImprimirVectores(["Santiago","Santiago","Santiago", "Laura","Laura", "Laura", "Laura","Pérez"], 2))

print(ImprimirVectores(["Santiago","Santiago","Santiago", "Laura", "Laura","Laura","Laura","Pérez","Pérez","Pérez","Santiago","Pedro"], 2))