def calcular_tiempo_total(lista_tiempos):
    '''
    calcular_tiempo_total
    toma una lista con tiempos de uso y los suma 
    Parameters
    ----------
    lista_tiempos : int
        una lista con numeros enteros positivos que represetan en tiempo de uso de x app.

    Returns
    -------
    float.
    el tiempo total de uso (la suma de todos los elementos de la lista)
    Raises: intexError = la lista esta vacia

    '''
    
    sumatoria = None
    if lista_tiempos == []:
        raise IndexError(f'la lista {lista_tiempos} esta vacia')
    else: 
        for numero in lista_tiempos:
            if sumatoria == None:
                  sumatoria = numero 
            else: 
                sumatoria += numero 
                return sumatoria


def calcular_promedio_uso(lista_usos):
    '''
    calcular_promedio_uso
    toma una lista de numeros, los suma y luego los divide por el lago de la lista

    Parameters
    ----------
    lista_usos : int
        una lista con numeros enteros que simbolizan cantidades de usp.

    Returns
    -------
    promedio : float.
    raises: indexError = la lsita esta vacia
    '''
    sumar = None
    if lista_usos == []:
       raise IndexError(f'la lista {lista_usos} esta vacia')
    else:
        for usos in lista_usos:
            if sumar == None:
                sumar = usos
            else:
                sumar += usos
        promedio = sumar / len(lista_usos)
        return promedio
        
            
        