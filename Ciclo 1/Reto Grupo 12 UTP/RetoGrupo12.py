def CalcularTotalBoletas(CantidadAdultos, CantidadMenores):
    ValorBoletaAdultos = 12000
    ValorBoletaMenores = 10000
    CantidadBoletas = CantidadAdultos + CantidadMenores

    Descuento = 0
    TotalAPagar = 0

    if CantidadBoletas == 2:
        Descuento = 10 / 100
        ValorTotalAdultos = ValorBoletaAdultos * CantidadAdultos
        ValorTotalAdultos = ValorTotalAdultos - round((Descuento * ValorTotalAdultos))
        ValorTotalMenores = ValorBoletaMenores * CantidadMenores
        ValorTotalMenores = ValorTotalMenores - round((Descuento * ValorTotalMenores))
    if CantidadBoletas == 3:
        Descuento = 15 / 100
        ValorTotalAdultos = ValorBoletaAdultos * CantidadAdultos
        ValorTotalAdultos = ValorTotalAdultos - round((Descuento * ValorTotalAdultos))
        ValorTotalMenores = ValorBoletaMenores * CantidadMenores
        ValorTotalMenores = ValorTotalMenores - round((Descuento * ValorTotalMenores))
    if CantidadBoletas == 4:
        Descuento = 20 / 100
        ValorTotalAdultos = ValorBoletaAdultos * CantidadAdultos
        ValorTotalAdultos = ValorTotalAdultos - round((Descuento * ValorTotalAdultos))
        ValorTotalMenores = ValorBoletaMenores * CantidadMenores
        ValorTotalMenores = ValorTotalMenores - round((Descuento * ValorTotalMenores))
    
    TotalAPagar = ValorTotalAdultos + ValorTotalMenores

    return f"El valor a pagar por adultos es: {ValorTotalAdultos} y por menores es: {ValorTotalMenores} para un total a pagar de: {TotalAPagar}."

CantidadAdultos = int(input("Ingrese la cantidad de adultos que van a ver la pelicula: "))
CantidadMenores  = int(input("Ingrese la cantidad de menores que van a ver la pelicula: "))

print(CalcularTotalBoletas(CantidadAdultos, CantidadMenores))