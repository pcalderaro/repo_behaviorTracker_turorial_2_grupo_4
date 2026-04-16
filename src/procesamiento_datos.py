def filtrar_por_participante(datos, id_participante):
    """
    Devuelve dos listas con los datos de un participante:
        - tiempos de uso
        - cantidades de uso
        
    datos: lista de diccionarios con los registros
    id_participante: id a filtrar
        
    return: (tiempos, cantidades)
        
    Raises:
        TypeError: si datos no es lista o los registros no son dict
        ValueError: si la lista está vacía
    """

if type(datos) != list:
    raise TypeError ("No es lista")

if len(datos) == []:
    raise ValueError ("La lista esta vacia")
    
tiempos = []
cantidades = []

for registro in datos:
    if "id_participante" in registro and "tiempo" in registro and "cantidad" in registro:
        if registro["id_participante"] == id_participante:
            tiempos.append(registro["tiempo"])
            cantidades.append(registro["cantidad"])

return tiempos, cantidades
