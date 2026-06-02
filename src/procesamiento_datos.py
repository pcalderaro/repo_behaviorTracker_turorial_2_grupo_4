import pandas as pd

def filtrar_por_participante(datos, id_participante):
    """
    Devuelve dos listas con los datos de un participante:
        - tiempos de uso
        - cantidades de uso
    datos: DataFrame de pandas con los registros
    id_participante: id a filtrar

    return: (tiempos, cantidades)
   
    Raises:
            TypeError: si datos no es un DataFrame de pandas
            ValueError: si el DataFrame está vacio
    """
 
    if type(datos) != pd.DataFrame:
        raise TypeError("No es lista")

    if datos.shape[0] == 0:
        raise ValueError("La lista esta vacia")

    datos_filtrados = datos.loc[datos["id_participante"] == id_participante]

    tiempos = datos_filtrados["tiempo_uso"].tolist()
    cantidades = datos_filtrados["cantidad_uso"].tolist()

    return tiempos, cantidades