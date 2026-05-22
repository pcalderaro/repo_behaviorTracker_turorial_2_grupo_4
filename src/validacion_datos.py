def validar_registro(registro):
    '''
    

    Parameters
    ----------
    registro : lista
        Recibe una lista y, si no esta vacía, se fija si sus datos son válidos o no. En el caso de ser válidos los almacena.
        
    Returns
    -------
    lista_datos_validos : lista
    None : None type
        Una vez recorrida la lista, devuelve una nueva lista solo con los datos váldios.

    '''
    if len(registro) == 0:
        return "la lista está vacía"
        
        lista_datos_validados = []
        contador = 0

        for i in range(cantidad):
            datos[id_participante] = {
                    "fecha": fecha,
                    "app": app,
                    "tiempo": tiempo
                                    }
            if es_dato_valido(dato) == True:
                lista_datos_validados.append(dato)
                contador += 1
            else:
                contador += 1
                raise ValueError("Error al validar un dato:")

        return lista_datos_validados

    else:
        raise Exception("Error en la función:")
        return None


def es_dato_valido(dato):
    '''

    Parameters
    ----------
    dato : int
        Toma valores y determina si cumplen con los parámetros para ser váldios o no

    Raises
    ------
    ValueError
        Ante cualquier error, avisa que no se pudo validar el dato

    Returns
    -------
    bool
        Si el dato es válido, devuelte True, si es invalido devuelve False

    '''
    try:
        if dato is None:
            return False
        
        elif dato == "":
            return False
        else:
            return True
        
    except Exception:
        raise ValueError("Error al validar el dato")
