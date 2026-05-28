from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_total
from src.metricas import calcular_promedio_uso

ruta = "datos/BehaviorTracker_mock_data.csv"


registros = cargar_datos(ruta) 


id_ingresado = input("Ingrese el ID del participante que desea filtrar: ")

try:
    id_buscado = int(id_ingresado)
    
    if id_buscado in registros:
      
        datos_participante = registros[id_buscado]
        try:
            tiempos, cantidades = filtrar_por_participante(datos_participante, id_buscado)
            
            resultado_tiempo_total = calcular_tiempo_total(tiempos)
            resultado_uso_promedio = calcular_promedio_uso(cantidades)
            
            print(f"Su tiempo total es de: {resultado_tiempo_total} y su cantidad promedio es de: {resultado_uso_promedio}")
            
        except TypeError as e:
            print(f"Error de tipo: {e}")
        except ValueError as e:
            print(f"Error de valor: {e}")
        except IndexError as e:
            print(f"Error en los índices: {e}")
    else:
        print(f"No se encontró ningún participante con el ID: {id_buscado}")

except ValueError:
    print("Por favor, ingrese un número de ID válido (entero).")

