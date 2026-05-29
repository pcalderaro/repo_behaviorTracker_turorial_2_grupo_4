from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_total
from src.metricas import calcular_promedio_uso
#ruta = "datos/BehaviorTracker_mock_data_error(nuemero).csv"
ruta = "datos/BehaviorTracker_mock_data.csv"


registros = cargar_datos(ruta) #dato = lista de dicionarios

id_buscado = input("Ingrese el ID del participante que desea filtrar: ")

if id_buscado in registros: # revisar, buscar por clave, es un dic
    participante = registros[id_buscado]
    print(participante)
       
    try:
         tiempos,cantidades = filtrar_por_participante(registros, id_buscado)
         print(tiempos)
         print(cantidades)
    except TypeError as e:
        print (e)
    except ValueError as e:
        print(e)
    else:
        try:        
            resultado_tiempo_total = calcular_tiempo_total(tiempos)
            resultado_uso_promedio = calcular_promedio_uso(cantidades)
        except IndexError as e:
            print(e)
        else:
            print(f"su tiempo total es de : {resultado_tiempo_total} y su cantidad promedio es de: {resultado_uso_promedio} ")


