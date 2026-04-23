def filtrar_por_participante(datos, id_participante): 
    '''

    Devuelve dos listas con los datos de un participante:

    - tiempos de uso

    - cantidades de uso

    datos: diccionario de diccionarios con los registros.

       Cada clave representa un registro y su valor es un diccionario

       con las claves: "id_participante", "tiempo" y "cantidad".

    id_participante: id a filtrar

    return: (tiempos, cantidades)

    Raises:

    TypeError: si datos no es un diccionario o si algún registro no es un diccionario

    ValueError: si el diccionario está vacío
    '''

    if type(datos) != dict:
        raise TypeError("No es diccionario")

    if len(datos) == 0:
        raise ValueError("El diccionario está vacío")

    tiempos = []
    cantidades = []

    for registro in datos.values():
        if type(registro) != dict:
            raise TypeError("Los registros deben ser diccionarios")

        if "id_participante" in registro and "tiempo" in registro and "cantidad" in registro:
            if registro["id_participante"] == id_participante:
                tiempos.append(registro["tiempo"])
                cantidades.append(registro["cantidad"])

    return tiempos, cantidades
