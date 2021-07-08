def agendamientoHornos(solicitudesHorneado: list) -> dict:
    Programacion = list()
    Itinerario = list()

    Itinerario.append(solicitudesHorneado[0])

    for i in range(1, len(solicitudesHorneado)):
        TiempoItinerario = 0
        for x in range(len(Itinerario)):
            TiempoItinerario += Itinerario[x]['tiempo']

        if Itinerario[-1]['tf'] <= solicitudesHorneado[i]['t0'] and (solicitudesHorneado[i]['tiempo'] + TiempoItinerario) <= 240:
            Itinerario.append(solicitudesHorneado[i])
        else:
            Programacion.append(list(Itinerario))
            Itinerario.clear()
            Itinerario.append(solicitudesHorneado[i])

    if Programacion[-1] != Itinerario:
        Programacion.append(list(Itinerario))

    Promedio = 0
    for i in range(len(solicitudesHorneado)):
        Promedio += solicitudesHorneado[i]['tiempo']

    Promedio = round(Promedio / len(Programacion), 2)

    return {'tiempoPromedioHornos': Promedio, 'hornosUtilizados': len(Programacion)}


""" ****************************Casos de prueba****************************** """

# print(agendamientoHornos([{'t0': 27, 'tf': 145, 'tiempo': 118, 'id': 'Proceso18'},  # 1
#                           {'t0': 28, 'tf': 91, 'tiempo': 63, 'id': 'Proceso1'},  # 2
#                           {'t0': 34, 'tf': 242, 'tiempo': 208,
#                               'id': 'Proceso19'},  # 3
#                           {'t0': 37, 'tf': 131, 'tiempo': 94,
#                               'id': 'Proceso20'},  # 4
#                           {'t0': 276, 'tf': 322, 'tiempo': 46,
#                               'id': 'Proceso12'},  # 4
#                           {'t0': 351, 'tf': 371, 'tiempo': 20,
#                               'id': 'Proceso17'},  # 4
#                           {'t0': 352, 'tf': 409, 'tiempo': 57,
#                               'id': 'Proceso14'},  # 5
#                           {'t0': 355, 'tf': 401, 'tiempo': 46,
#                               'id': 'Proceso15'},  # 6
#                           {'t0': 551, 'tf': 604, 'tiempo': 53,
#                               'id': 'Proceso3'},  # 6
#                           {'t0': 572, 'tf': 632, 'tiempo': 60,
#                               'id': 'Proceso4'},  # 7
#                           {'t0': 589, 'tf': 635, 'tiempo': 46,
#                               'id': 'Proceso6'},  # 8
#                           {'t0': 612, 'tf': 635, 'tiempo': 23,
#                               'id': 'Proceso8'},  # 9
#                           {'t0': 623, 'tf': 644, 'tiempo': 21,
#                               'id': 'Proceso9'},  # 10
#                           {'t0': 648, 'tf': 726, 'tiempo': 78,
#                               'id': 'Proceso10'},  # 10
#                           {'t0': 927, 'tf': 991, 'tiempo': 64,
#                               'id': 'Proceso2'},  # 10
#                           {'t0': 940, 'tf': 982, 'tiempo': 42,
#                               'id': 'Proceso5'},  # 11
#                           {'t0': 964, 'tf': 1009, 'tiempo': 45,
#                               'id': 'Proceso7'},  # 12
#                           {'t0': 1056, 'tf': 1085, 'tiempo': 29,
#                               'id': 'Proceso11'},  # 12
#                           {'t0': 1262, 'tf': 1282, 'tiempo': 20,
#                               'id': 'Proceso13'},  # 12
#                           {'t0': 1298, 'tf': 1320, 'tiempo': 22, 'id': 'Proceso16'}]))  # 12

"""Resultado esperado => {'tiempoPromedioHornos': 96.25, 'hornosUtilizados': 12} """

""" print(agendamientoHornos([{'t0': 2, 'tf': 182, 'tiempo': 180, 'id': 'Tarea19'},
                          {'t0': 2, 'tf': 144, 'tiempo': 142, 'id': 'Tarea20'},
                          {'t0': 411, 'tf': 449, 'tiempo': 38, 'id': 'Tarea2'},
                          {'t0': 474, 'tf': 512, 'tiempo': 38, 'id': 'Tarea14'},
                          {'t0': 493, 'tf': 515, 'tiempo': 22, 'id': 'Tarea7'},
                          {'t0': 538, 'tf': 579, 'tiempo': 41, 'id': 'Tarea1'},
                          {'t0': 550, 'tf': 571, 'tiempo': 21, 'id': 'Tarea4'},
                          {'t0': 572, 'tf': 589, 'tiempo': 17, 'id': 'Tarea8'},
                          {'t0': 577, 'tf': 611, 'tiempo': 34, 'id': 'Tarea10'},
                          {'t0': 580, 'tf': 612, 'tiempo': 32, 'id': 'Tarea13'},
                          {'t0': 600, 'tf': 628, 'tiempo': 28, 'id': 'Tarea15'},
                          {'t0': 607, 'tf': 624, 'tiempo': 17, 'id': 'Tarea17'},
                          {'t0': 619, 'tf': 636, 'tiempo': 17, 'id': 'Tarea18'},
                          {'t0': 1091, 'tf': 1128, 'tiempo': 37, 'id': 'Tarea16'},
                          {'t0': 1120, 'tf': 1141, 'tiempo': 21, 'id': 'Tarea3'},
                          {'t0': 1136, 'tf': 1171, 'tiempo': 35, 'id': 'Tarea5'},
                          {'t0': 1140, 'tf': 1159, 'tiempo': 19, 'id': 'Tarea6'},
                          {'t0': 1166, 'tf': 1212, 'tiempo': 46, 'id': 'Tarea11'},
                          {'t0': 1172, 'tf': 1189, 'tiempo': 17, 'id': 'Tarea12'},
                          {'t0': 1265, 'tf': 1285, 'tiempo': 20, 'id': 'Tarea9'}])) """

"""Resultado esperado => {'tiempoPromedioHornos': 63.23, 'hornosUtilizados': 13} """

""" print(agendamientoHornos([{'t0': 4, 'tf': 65, 'tiempo': 61, 'id': 'P19'}, #1
                          {'t0':6, 'tf': 68, 'tiempo': 62, 'id': 'P20'}, #2
                          {'t0': 272, 'tf': 296, 'tiempo': 24, 'id': 'P6'},#2
                          {'t0': 350, 'tf': 388, 'tiempo': 38, 'id': 'P7'}, #2
                          {'t0': 375, 'tf': 393, 'tiempo': 18, 'id': 'P10'},#3
                          {'t0': 385, 'tf': 405, 'tiempo': 20, 'id': 'P12'},#4
                          {'t0': 435, 'tf': 455, 'tiempo': 20, 'id': 'P5'},#4
                          {'t0': 566, 'tf': 582, 'tiempo': 16, 'id': 'P9'},#4
                          {'t0': 646, 'tf': 666, 'tiempo': 20, 'id': 'P11'},#4
                          {'t0': 688, 'tf': 707, 'tiempo': 19, 'id': 'P3'},#4
                          {'t0': 692, 'tf': 709, 'tiempo': 17, 'id': 'P4'},#5
                          {'t0': 725, 'tf': 742, 'tiempo': 17, 'id': 'P8'},#5
                          {'t0': 756, 'tf': 780, 'tiempo': 24, 'id': 'P13'},#5
                          {'t0': 759, 'tf': 787, 'tiempo': 28, 'id': 'P16'},#6
                          {'t0': 773, 'tf': 792, 'tiempo': 19, 'id': 'P1'},#7
                          {'t0': 832, 'tf': 849, 'tiempo': 17, 'id': 'P2'},#7
                          {'t0': 871, 'tf': 888, 'tiempo': 17, 'id': 'P18'},#7
                          {'t0': 922, 'tf': 945, 'tiempo': 23, 'id': 'P14'},#7
                          {'t0': 1008, 'tf': 1026, 'tiempo': 18, 'id': 'P17'},#8
                          {'t0': 1083, 'tf': 1100, 'tiempo': 17, 'id': 'P15'}]))#9 """

"""Resultado esperado => {'tiempoPromedioHornos': 116.89, 'hornosUtilizados': 9} """

# print(agendamientoHornos([{'t0': 4, 'tf': 65, 'tiempo': 61, 'id': 'P19'}, {'t0': 6, 'tf': 68, 'tiempo': 62, 'id': 'P20'}, {'t0': 272, 'tf': 296, 'tiempo': 24, 'id': 'P6'}, {'t0': 350, 'tf': 388, 'tiempo': 38, 'id': 'P7'}, {'t0': 375, 'tf': 393, 'tiempo': 18, 'id': 'P10'}, {'t0': 385, 'tf': 405, 'tiempo': 20, 'id': 'P12'}, {'t0': 435, 'tf': 455, 'tiempo': 20, 'id': 'P5'}, {'t0': 566, 'tf': 582, 'tiempo': 16, 'id': 'P9'}, {'t0': 646, 'tf': 666, 'tiempo': 20, 'id': 'P11'}, {'t0': 688, 'tf': 707, 'tiempo': 19, 'id': 'P3'}, {
#       't0': 692, 'tf': 709, 'tiempo': 17, 'id': 'P4'}, {'t0': 725, 'tf': 742, 'tiempo': 17, 'id': 'P8'}, {'t0': 756, 'tf': 780, 'tiempo': 24, 'id': 'P13'}, {'t0': 759, 'tf': 787, 'tiempo': 28, 'id': 'P16'}, {'t0': 773, 'tf': 792, 'tiempo': 19, 'id': 'P1'}, {'t0': 832, 'tf': 849, 'tiempo': 17, 'id': 'P2'}, {'t0': 871, 'tf': 888, 'tiempo': 17, 'id': 'P18'}, {'t0': 922, 'tf': 945, 'tiempo': 23, 'id': 'P14'}, {'t0': 1008, 'tf': 1026, 'tiempo': 18, 'id': 'P17'}, {'t0': 1083, 'tf': 1100, 'tiempo': 17, 'id': 'P15'}]))


print(agendamientoHornos([{'t0': 16, 'tf': 255, 'tiempo': 239, 'id': 'P19'}, {'t0': 22, 'tf': 148, 'tiempo': 126, 'id': 'P20'}, {'t0': 196, 'tf': 217, 'tiempo': 21, 'id': 'P12'}, {'t0': 349, 'tf': 376, 'tiempo': 27, 'id': 'P7'}, {'t0': 381, 'tf': 408, 'tiempo': 27, 'id': 'P9'}, {'t0': 478, 'tf': 549, 'tiempo': 71, 'id': 'P18'}, {'t0': 487, 'tf': 535, 'tiempo': 48, 'id': 'P1'}, {'t0': 539, 'tf': 567, 'tiempo': 28, 'id': 'P2'}, {'t0': 561, 'tf': 604, 'tiempo': 43, 'id': 'P4'}, {'t0': 621, 'tf': 663, 'tiempo': 42, 'id': 'P8'}, {
      't0': 652, 'tf': 701, 'tiempo': 49, 'id': 'P16'}, {'t0': 658, 'tf': 703, 'tiempo': 45, 'id': 'P15'}, {'t0': 817, 'tf': 845, 'tiempo': 28, 'id': 'P11'}, {'t0': 829, 'tf': 858, 'tiempo': 29, 'id': 'P13'}, {'t0': 957, 'tf': 984, 'tiempo': 27, 'id': 'P5'}, {'t0': 1037, 'tf': 1065, 'tiempo': 28, 'id': 'P14'}, {'t0': 1090, 'tf': 1159, 'tiempo': 69, 'id': 'P17'}, {'t0': 1215, 'tf': 1259, 'tiempo': 44, 'id': 'P6'}, {'t0': 1309, 'tf': 1344, 'tiempo': 35, 'id': 'P10'}, {'t0': 1422, 'tf': 1448, 'tiempo': 26, 'id': 'P3'}]))
