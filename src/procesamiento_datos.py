def filtrar_por_participante(datos, id_participante):
    """
    Devuelve dos listas con los datos de un participante:
    - tiempos de uso
    - cantidades de uso

    datos: lista de diccionarios con los registros
    id_participante: id a filtrar

    return: (tiempos, cantidades)
    """

    tiempos = []
    cantidades = []

    for registro in datos:
        if registro["id_participante"] == id_participante:
            tiempos.append(registro["tiempo"])
            cantidades.append(registro["cantidad"])

    return tiempos, cantidades
