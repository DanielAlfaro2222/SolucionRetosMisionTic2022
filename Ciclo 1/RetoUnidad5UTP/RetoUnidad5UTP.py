from os import set_inheritable
import matplotlib as plt


def analisisTRM(rutaArchivo: str) -> dict:

    import pandas as pd

    # Verificar al extension del archivo
    if rutaArchivo[-3:].lower() != 'csv':
        return "Extensión inválida"

    # Intentar abrir el archivo, sino cortar la funcion con un mensaje de error
    try:
        df = pd.read_csv(rutaArchivo, sep=',')
    except:
        return "Error al leer el archivo de datos"

    # Convertir el campo fecha al tipo fecha de pandas
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)

    # Pasar el campo fecha como indice de los registros
    df.set_index('Fecha', inplace=True)

    Serie = pd.Series([((abs(df['TRM'][i - 1] - df['TRM'][i]) /
                         df['TRM'][i - 1]) * 100) for i in range(1, len(df))])

    Promedio = round(sum(Serie) / len(Serie), 16)

    PromedioCasos = sum(df['Casos']) / len(df['Casos'])

    RegistrosMayores = df[df['Casos'] >= PromedioCasos]

    return {'Promedio Variación': Promedio, 'Registros Mayores': RegistrosMayores}


print(analisisTRM('https://raw.githubusercontent.com/luismescobarf/clasesCiclo1/master/BaseDeDatosReto5.csv'))

"""
Visualizacion 1

dataCasosMes = data["Casos"].groupby(data.index.month).sum()
dataCasosMes.plot(color="red")
plt.title("Total casos por mes")
plt.xlabel("Mes")
plt.ylabel("Número de casos")
plt.show()
"""

"""
Visualizacion 2

dataMediaPrecioMes = data['TRM'].groupby(data.index.month).mean()
dataMediaPrecioMes.plot(color = "green")
plt.title("Valor dólar promedio")
plt.xlabel("Mes")
plt.ylabel("Valor")
plt.show()
"""
