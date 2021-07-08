"""
-----------------------------------------------------------------------------------------------------------------
Objetivo

Crear una funcion que permita crear clientes, añadir facturas, abonar a las facturas y llaver una base de datos con toda la informacion por cliente.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Pseudocodigo

1.Crear un diccionario vacio, el cual sera donde se almacene la informacion de la base de datos.
2.Crear una funcion que reciba como parametro opcion, id cliente, numero de la factura, el valor, y el diccionario de la base de datos.
3.En la funcion implementar el arbol de desiciones que previamente se creo.
4.Imprimir y llamar a la funcion.
"""

"""
Diccionarios

1. El primer diccionario contiene el mensaje del sistema.
2. El segundo diccionario contiene el estado de la base de datos.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Traduccion al lenguaje python
"""

def funcion(Opcion: int, IdCliente: int = 0, NumeroFactura: int = 0, Valor: int = 0,Db: dict = {})->dict:
    BusquedaCliente = False
    BusquedaFactura = False

    if Opcion == 0:
        if NumeroFactura != 0 and Valor != 0:
            return "Mensaje del aplicativo: " + str({IdCliente:'No existe el cliente'}) + "\nEstado de la base de datos: " + str(Db) + "\n"
        else:
            Db[IdCliente] = {}
            return "Mensaje del aplicativo: " + str({IdCliente:'Cliente creado'}) + "\nEstado de la base de datos: " + str(Db) + "\n"
    elif Opcion == 1:
        #Buscar cliente en la lista, si lo encuentra, cambia el valor de la variable BusquedaCliente por True
        ListaClientes = list(Db.keys())
        for i in range(len(ListaClientes)):
            if IdCliente == ListaClientes[i]:
                BusquedaCliente = True

        if BusquedaCliente:
            Db[IdCliente].update({NumeroFactura: Valor})
            return "Mensaje del aplicativo: " + str({'Cliente': IdCliente, 'Factura': NumeroFactura, 'Abono': 0, 'Valor': Valor}) + "\nEstado de la base de datos: " + str(Db) + "\n"
        else:
            return "Mensaje del aplicativo: " + str({IdCliente:'No existe el cliente'}) + "\nEstado de la base de datos: " + str(Db) + "\n"
    elif Opcion == 2:
        #Buscar cliente en la lista, si lo encuentra, cambia el valor de la variable BusquedaCliente por True
        ListaClientes = list(Db.keys())
        for i in range(len(ListaClientes)):
            if IdCliente == ListaClientes[i]:
                BusquedaCliente = True
        if BusquedaCliente:
            ListaFacturas = list(Db[IdCliente].keys())
            for j in range(len(ListaFacturas)):
                if NumeroFactura == ListaFacturas[j]:
                    BusquedaFactura = True

            if BusquedaFactura:
                if (Valor - Db[IdCliente][NumeroFactura]) == 0:
                    del Db[IdCliente][NumeroFactura]
                    return "Mensaje del aplicativo: " + str({'Cliente': IdCliente, 'Factura': NumeroFactura, 'Abono': Valor, 'Valor': 0.0}) + "\nEstado de la base de datos: " + str(Db) + "\n"
                else:
                    Db[IdCliente][NumeroFactura] = Db[IdCliente][NumeroFactura] - Valor
                    return "Mensaje del aplicativo: " + str({'Cliente': IdCliente, 'Factura': NumeroFactura, 'Abono': Valor, 'Valor': Db[IdCliente][NumeroFactura]}) + "\nEstado de la base de datos: " + str(Db) + "\n"
            else:
               return "Mensaje del aplicativo: " + str({IdCliente:'No existe la factura'}) + "\nEstado de la base de datos: " + str(Db) + "\n"
            
        else:
            return "Mensaje del aplicativo: " + str({IdCliente:'No existe el cliente'}) + "\nEstado de la base de datos: " + str(Db) + "\n"
    elif Opcion == 3:
        return "Estado de la base de datos: " + str(Db) + "\n"

""" diccionario = dict(uno = dict())
diccionario['uno'] = {'uno': 'dos'}

diccionario['uno'].update({'tres': 'cuatro'})

print(diccionario) """

print(funcion(Opcion = 0, IdCliente = 2541, NumeroFactura = 0, Valor = 0))
print(funcion(Opcion = 1, IdCliente = 2541, NumeroFactura = 1, Valor = 300000))
print(funcion(Opcion = 2, IdCliente = 2541, NumeroFactura = 1, Valor = 25000.25487))
print(funcion(Opcion = 1, IdCliente = 2541, NumeroFactura = 2, Valor = 500000))
print(funcion(Opcion = 2, IdCliente = 1429, NumeroFactura = 5, Valor = 25000.25487))
print(funcion(Opcion = 1, IdCliente = 1429, NumeroFactura = 1, Valor = 700000))
print(funcion(Opcion = 2, IdCliente = 1429, NumeroFactura = 1, Valor = 700000))
print(funcion(Opcion = 0, IdCliente = 1429, NumeroFactura = 1, Valor = 700000))
print(funcion(Opcion = 0, IdCliente = 1429, NumeroFactura = 0, Valor = 0))
print(funcion(Opcion = 1, IdCliente = 1429, NumeroFactura = 1, Valor = 700000))
print(funcion(Opcion = 2, IdCliente = 2541, NumeroFactura = 1, Valor = 274999.74513))
print(funcion(Opcion = 3, IdCliente = 0, NumeroFactura = 0, Valor = 0))