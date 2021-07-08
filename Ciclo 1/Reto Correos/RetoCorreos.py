import pprint as pp


def ValidarFuncionario(diccionario: dict) -> tuple:

    # Filtrar el listado de las personas activas con su par clave-valor
    def PredicadoFiltradoDiccionario(elemento):
        return elemento[-1]['areas'][0]['activo'] == 'si'

    FiltradoPersonasActivas = list(
        filter(PredicadoFiltradoDiccionario, list(diccionario.items())))

    # Crear el diccionario final donde se muestra la informacion de las personas activas
    DiccionarioPersonasActivas = dict()

    for elemento in FiltradoPersonasActivas:
        DiccionarioPersonasActivas[elemento[0]] = elemento[-1]

    # Crear el correo a las personas activas
    ListadoCorreos = list()

    for elemento in FiltradoPersonasActivas:
        Nombre = str(elemento[-1]['nombres'][0].lower())
        Apellido = elemento[-1]['apellidos'].lower().split(',')
        ListadoCorreos.append(f"{Nombre}.{Apellido[0]}.gmail.com")

    return (ListadoCorreos, DiccionarioPersonasActivas)


funcionario1 = {
    10852758781: {
        "nombres": "Juana",
        "apellidos": "Gomez, Lopez",
        "annio_ingreso": 2000,
        "dependencia": "Rectoria",
        "areas": [{
            "nombre": "Secretaria",
            "codigo": 1,
            "activo": "si"}
        ],
    },
    1010275871: {
        "nombres": "Pepito Carlos",
        "apellidos": "Mendieta, Castillo",
        "annio_ingreso": 2003,
        "dependencia": "Rectoria",
        "areas": [{
            "nombre": "Tesoreria",
            "codigo": 2,
            "activo": "si"}
        ],
    },
    10102758715: {
        "nombres": "Miguel Angel",
        "apellidos": "Suarez, Quiroz",
        "annio_ingreso": 2005,
        "dependencia": "Rectoria",
        "areas": [{
            "nombre": "Tesoreria",
            "codigo": 2,
            "activo": "si"}
        ],
    },
    10122758089: {
        "nombres": "Luisa Paula",
        "apellidos": "Fajardo, Fernandez",
        "annio_ingreso": 2005,
        "dependencia": "Vicerrectoria",
        "areas": [
            {
                "nombre": "Academica",
                "codigo": 11,
                "activo": "si"
            },
        ]
    },
    101227580874: {
        "nombres": "Pablo Luis",
        "apellidos": "Jojoa, Ruiz",
        "annio_ingreso": 1999,
        "dependencia": "Vicerrectoria",
        "areas": [
            {
                "nombre": "Administrativa",
                "codigo": 12,
                "activo": "no"
            },
        ]}
}

funcionario2 = {
    1085273521: {
        "nombres": "Johana",
        "apellidos": "Gomez, Lopez",
        "annio_ingreso": 2000,
        "dependencia": "Rectoria",
        "areas": [
            {
                "nombre": "Secretaria",
                "codigo": 1,
                "activo": "no"
            },
        ]
    },
    1010275872: {
        "nombres": "Juan Carlos",
        "apellidos": "Mendieta, Castillo",
        "annio_ingreso": 2003,
        "dependencia": "Rectoria",
        "areas": [
            {
                "nombre": "Tesoreria",
                "codigo": 2,
                "activo": "no"
            },
        ]
    },
    1010375891: {
        "nombres": "Miguel Angel",
        "apellidos": "Suarez, Quiroz",
        "annio_ingreso": 2005,
        "dependencia": "Rectoria",
        "areas": [
            {
                "nombre": "Tesoreria",
                "codigo": 2,
                "activo": "no"
            },
        ]
    },
    1012025802: {
        "nombres": "Silvia Lorena",
        "apellidos": "Fajardo, Melo",
        "annio_ingreso": 2005,
        "dependencia": "Vicerrectoria",
        "areas": [
            {
                "nombre": "Academica",
                "codigo": 11,
                "activo": "no"
            },
        ]
    }, 1085242433: {
        "nombres": "Gloria Sofia",
        "apellidos": "Jojoa, Ruiz",
        "annio_ingreso": 1999,
        "dependencia": "Vicerrectoria",
        "areas": [
            {
                "nombre": "Administrativa",
                "codigo": 12,
                "activo": "no"
            },
        ]
    }
}

pp.pprint(ValidarFuncionario(funcionario1))
# print(ValidarFuncionario(funcionario2))
