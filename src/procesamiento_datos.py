def filtrar_por_participante(datos, id_participante):
    """
    Devuelve dos listas con los datos de un participante:
    - tiempos de uso
    - cantidades de uso

    datos: lista de diccionarios con los registros
    id_participante: id a filtrar

    return: (tiempos, cantidades)
    """
    if type(datos) != list:
        raise TypeError("datos debe ser una lista")

    if type(id_participante) != int:
        raise TypeError("id_participante debe ser un entero")

    for i, registro in enumerate(datos):
        if type(registro) != dict:
            raise TypeError(f"El elemento en posición {i} no es un diccionario")

        if ("id_participante" not in registro or
            "tiempo" not in registro or
            "cantidad" not in registro):
            raise KeyError(f"Faltan claves en el registro en posición {i}")

    tiempos = []
    cantidades = []

    for registro in datos:
        if registro["id_participante"] == id_participante:
            tiempos.append(registro["tiempo"])
            cantidades.append(registro["cantidad"])

    return tiempos, cantidades
