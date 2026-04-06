from scr.validacion_datos import validar_registro
def parsear_linea(linea): 
    '''
    Convierte una linea de texto del archivo en un registro con los tipos de datos correspondientes. 

    Parameters
    ----------
    linea : str
        Linea del archivo a procesar

    Returns
    -------
   list
   Lista con los datos convertidos
   [id_participante, fecha, app, cantidad_uso, tiempo_uso]
   
   Lanza
   ------
   ValueError
       Si la linea no tiene exactamnte 5 campos. 
    '''
    datos = linea.spli(",")
    
    if len(datos) != 5: 
        raise ValueError ("La linea no tiene 5 campos")
    
    id_participante= int(datos[0])
    fecha= datos[1]
    app= datos[2]
    cantidad_uso= int(datos[3])
    tiempo_uso= float(datos[4])
    registro = [id_participante,fecha,app,cantidad_uso,tiempo_uso]
    registro_valido =validar_registro(registro)
    
    return registro_valido

def cargar_datos (archivo): 
    '''
    Lee un archivo de texto, procesa cada linea valida y devuelve una lista con todos los registros cargados. 
    
    La funcion: abre el archivo. recorre cada linea, ignora las lineas vacias, usa parsear_lineas() para transformar cada liena y guarda los registros validos en una lista
    

    Parameters
    ----------
    archivo : str
       Nombre del archivo a leer

    Returns
    -------
    list
        Lista con los registros validos cargados desde el archivo. 
    

    '''
    registros=[]
    
    archivo=open(archivo, "r", encoding="utf-8")
    
    for linea in archivo: 
        linea=linea.strip()
        
        if linea != "": 
            try: 
                registro=parsear_linea(linea)
                registros.append(registro)
            except ValueError: 
                print("Error en la linea", linea)
    archivo.close()
    return registros 
    
