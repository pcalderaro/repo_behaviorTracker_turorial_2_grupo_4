def filtrar_por_participante(datos: list, id_participante; int):
    """
    Filtra los registros que pertenecen a un participante especifico.

    Parametros:
    datos : lista de diccionarios
    id_participante: int

    Retorna:
    lista de diccionarios filtrados
    """
    resultado = [ ]
    
    for registro in datos:
        if registro ["id_participante"] == id_participante:
            resultado.append(registro)
    
    return resultado
