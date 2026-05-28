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

    filas_validas = []

    for i in range(len(df)):

        registro = [
            int(df.iloc[i,0]),
            df.iloc[i,1],
            df.iloc[i,2],
            int(df.iloc[i,3]),
            float(df.iloc[i,4])
        ]

        try:

            for dato in registro:
                validar_registro(registro, dato)

            filas_validas.append(registro)

        except ValueError:
            print("Registro inválido:", registro)

    df_final = pd.DataFrame(
        filas_validas,
        columns=["id_participante", "fecha", "app", "cantidad_uso", "tiempo_uso"]
    )

    return df_final
  
