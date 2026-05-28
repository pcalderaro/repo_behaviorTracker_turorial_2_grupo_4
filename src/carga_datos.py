from src.validacion_datos import validar_registro
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
   
   Raise
   ------
   ValueError
       Si la linea no tiene exactamnte 5 campos. 
    '''
    datos = linea.split(",")
    
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
    registros={}
    if archivo == " ": 
        raise ValueError ("El nomre del archivo no puede estar vacio")
    
    archivo=open(archivo, "r", encoding="utf-8")
    
    for linea in archivo: 
        linea=linea.strip()
        
        if linea != "": 
            
            registro=parsear_linea(linea)

            id_participante= registro[0]
            fecha= registro[1]
            app= registro[2]
            cantidad_uso= registro[3]
            tiempo_uso= registro[4]

            if id_participante not in registros: 
                registros[id_participante]={"ID": id_participante,
                    "fecha": [],
                    "app": [],
                    "cantidad de uso": [],
                    "tiempo de uso": []}
              
                registros[id_participante]["fecha"].append(fecha)
                registros[id_participante]["app"].append(app)
                registros[id_participante]["cantidad de uso"].append(cantidad_uso)
                registros[id_participante]["tiempo de uso"].append(tiempo_uso)
            

            
    archivo.close()
    return registros 
    
#registro=parsear_linea(linea), si hay algo invalido, parsear_linea() lanza ValueError y automaticamnte se corta cargar_datos(). 
