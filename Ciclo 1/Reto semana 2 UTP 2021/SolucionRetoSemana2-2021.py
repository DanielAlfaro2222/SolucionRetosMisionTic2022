""" 
-----------------------------------------------------------------------------------------------------------------
Problema

Una marca deportiva está interesada en contratar los tenistas con mejor rendimiento de cada rama profesional ATP, como imágenes de la nueva línea de productos que lanzará la próxima temporada, para ello, ha contratado a un equipo de analistas deportivos, quienes a través de los años, han identificado elementos clave para pronosticar con precisión, los jugadores más opcionados a alcanzar la posición número 1 del ranking profesional de cada rama. Los factores que los expertos encuentran determinantes son los siguientes:

    * Partidos Ganados.
    * Partidos Perdidos.
    * Puntos acumulados en su Ranking ATP.
    * Promedio de Dobles faltas por partido.
    * Ganador en Olímpicos.
    * Número de Torneos jugados.
    * Promedio de Saques perfectos o aces. 

En el estudio realizado por los expertos, las mencionadas variables han sido relacionadas. El árbol de decisiones de la Figura 1, muestra dicha relación cómo influye en la probabilidad de que cada jugador de cualquiera de las dos ramas, alcance la posición número 1 en el ranking mundial.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Objetivo

Se requiere entonces, implementar una función que recibiendo las estadísticas recolectadas de un jugador de cualquiera de las dos ramas, y encapsuladas en un diccionario, retorne las probabilidades de que este jugador o jugadora alcance la posición número 1 en el ranking mundial, generando un mensaje de la forma “La jugadora {nombre} tiene 0.8 de probabilidad de quedar primera en el ranking ATP” o “El jugador {nombre} tiene 0.65
de probabilidad de quedar primero en el ranking ATP”, donde el porcentaje corresponde a la clasificación que ha determinado el árbol de decisiones.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Pseudocodigo

1.Crear un diccionario con los datos del participante(en los casos de prueba esta los datos de los cuatro participantes).

2.Crear una funcion de conversion de tipos para el sexo y olimpicos, el sexo y olimpicos deben quedar de tipo boolean, esta funcion recibira como parametro el diccionario con los datos del participante y retornara los datos ya convertidos.

3.Crear la funcion que calcule el pronostico de el participante de la ATP, esta funcion recibira como parametro el diccionario con los datos del participante.

4.Implementar arbol de decision

5.Retornar segun el sexo del participante el promedio y el siguiente mensaje  “La jugadora {nombre} tiene 0.8 de probabilidad de quedar primera en el ranking ATP” o “El jugador {nombre} tiene 0.65 de probabilidad de quedar primero en el ranking ATP”.

6.Imprimir y llamar a la funcion principal y pasarle como parametro el diccionario con los datos del participante.
"""

"""
-----------------------------------------------------------------------------------------------------------------
Traduccion a Python
"""
def pronosticoATP(jugador: dict):
    Sexo = jugador["sexo"] == "mujer"
    Olimpicos = False

    if (jugador["Olimpicos"] == "Oro") or (jugador["Olimpicos"] == "Plata") or(jugador["Olimpicos"] == "Bronce"):
        Olimpicos = True

    RankingATP = jugador["Ranking ATP"]
    DoblesFaltas = jugador["Dobles faltas"]
    TorneosJugados = jugador["Torneos jugados"]
    SaquesPerfectos = jugador["Saques perfectos"]
    Nombre = jugador["nombre"]
    PartidoGanado = jugador["PG"]
    PartidoPerdido = jugador["PP"]

    if Sexo:
        if (PartidoGanado > PartidoPerdido) or (RankingATP > 2400):
            if not(DoblesFaltas > 4) and (TorneosJugados > 19):
                if Olimpicos:
                    return f"La jugadora {Nombre} tiene 0.8 de probabilidad de quedar primera en el ranking ATP"
                else:
                    return f"La jugadora {Nombre} tiene 0.65 de probabilidad de quedar primera en el ranking ATP"
            else:
                return f"La jugadora {Nombre} tiene 0.5 de probabilidad de quedar primera en el ranking ATP"
        else:
            if (TorneosJugados <= 18) and (DoblesFaltas > 5):
                return f"La jugadora {Nombre} tiene 0.5 de probabilidad de quedar primera en el ranking ATP"
            else:
                return f"La jugadora {Nombre} tiene 0.6 de probabilidad de quedar primera en el ranking ATP"
    else:
        if Olimpicos:
            if (PartidoGanado > PartidoPerdido) and (TorneosJugados > 17):
                if (DoblesFaltas < 4) or (SaquesPerfectos > 7):
                    return f"El jugador {Nombre} tiene 0.8 de probabilidad de quedar primero en el ranking ATP"
                else:
                    return f"El jugador {Nombre} tiene 0.7 de probabilidad de quedar primero en el ranking ATP"
            else:
                if RankingATP > 2400:
                    return f"El jugador {Nombre} tiene 0.65 de probabilidad de quedar primero en el ranking ATP"
                else:
                    return f"El jugador {Nombre} tiene 0.55 de probabilidad de quedar primero en el ranking ATP"
        else:
            if (RankingATP > 2200) or (TorneosJugados > 18):
                if (DoblesFaltas < 4) and (PartidoGanado > PartidoPerdido):
                    return f"El jugador {Nombre} tiene 0.55 de probabilidad de quedar primero en el ranking ATP"
                else:
                    return f"El jugador {Nombre} tiene 0.45 de probabilidad de quedar primero en el ranking ATP"
            else:
                return f"El jugador {Nombre} tiene 0.35 de probabilidad de quedar primero en el ranking ATP"


"""
-----------------------------------------------------------------------------------------------------------------
Casos de prueba
"""

print(pronosticoATP({"nombre":"Serena Williams", "sexo": "mujer","PG": 5,"PP": 2, "Olimpicos": "Oro", "Ranking ATP": 3000, "Dobles faltas" : 3, "Torneos jugados": 23, "Saques perfectos": 10}))

print(pronosticoATP({"nombre":"Roger Federer", "sexo": "hombre","PG": 5,"PP": 3,"Olimpicos": "Plata", "Ranking ATP": 2200, "Dobles faltas": 5, "Torneos jugados": 18, "Saques perfectos": 6}))

print(pronosticoATP({"nombre":"Simona Halep", "sexo": "mujer","PG": 2,"PP": 3,"Olimpicos": "Plata", "Ranking ATP": 2200, "Dobles faltas": 6, "Torneos jugados": 18, "Saques perfectos": 10}))

print(pronosticoATP({"nombre": "Yannick Hanfmann", "sexo": "hombre","PG" :1,"PP": 7, "Olimpicos": "No Participante", "Ranking ATP": 819, "Dobles faltas": 7, "Torneos jugados": 10, "Saques perfectos": 2}))
