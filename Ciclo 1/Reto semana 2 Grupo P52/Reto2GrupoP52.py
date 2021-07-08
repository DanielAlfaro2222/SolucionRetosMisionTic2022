"""
-----------------------------------------------------------------------------------------------------------------
Objetivo

Escriba una función que reciba como parámetros: un diccionario con los precios por unidad de cada tipo de bola, una cadena con el sabor del helado que se quiere comprar, el número de bolas que quiere comprar y retorne una cadena que represente el valor de la compra. La cadena debe tener la siguiente estructura: “Debe pagar en total {valor}” donde, el valor debe cumplir con las especificaciones mencionadas anteriormente (número de bolas multiplicado por el valor que le corresponda pagar según el sabor del helado).
"""

PrecioUnidadHelados = dict(Chocolate = 1500, Vainilla = 850, Fresa = 500)


def CompraHelado(PrecioUnidadHelados: dict, SaborHelado: str, NumeroBolas: int) -> str:
    TotalAPagar = 0

    if SaborHelado == "Chocolate":
        TotalAPagar = PrecioUnidadHelados['Chocolate'] * NumeroBolas
    elif SaborHelado == "Vainilla":
        TotalAPagar = PrecioUnidadHelados['Vainilla'] * NumeroBolas
    elif SaborHelado == "Fresa":
        TotalAPagar = PrecioUnidadHelados['Fresa'] * NumeroBolas

    return f"Debe pagar en total {TotalAPagar}"

print(CompraHelado(PrecioUnidadHelados, "Chocolate", 3))