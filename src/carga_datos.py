import pandas as pd
from src.validacion_datos import validar_registro


def cargar_datos (archivo): 
    '''
    Lee un archivo de texto, procesa cada linea valida y devuelve un diccionario con los datos agrupados por participante. 

    Si el id ya exsiste, agrega los nuevos datos en las listas. 
    Si el id no exsiste, crea su estrucutra y luego agrega los datos. 
    

    Parameters
    ----------
    archivo : str
       Nombre del archivo a leer

    Returns
    -------
   dict
       Diccionario con los datos agrupados por id. 

    Raises
    --------
    ValueError 
        Si el nombre del archivo esta vacio. 
    FileNotFound
        Si el archivo no existe. 
    

    '''
    
    if archivo == " ": 
        raise ValueError ("El nomre del archivo no puede estar vacio")
    
    df = pd.read_csv(
        archivo,
        header=None,
        names=["id_participante", "fecha", "app", "cantidad_uso", "tiempo_uso"],
        dtype={
            "id_participante": int,
            "app":             str,
            "cantidad_uso":    int,
            "tiempo_uso":      float,
        },
    )
    df = df.dropna()
    #para eliminar las filas vacias
    return df.dropna()
