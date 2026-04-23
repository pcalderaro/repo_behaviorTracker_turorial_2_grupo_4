from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_total
from src.metricas import calcular_promedio_uso
# ruta = "datos/BehaviorTracker_mock_data_error(nuemero).csv"
ruta = "datos/BehaviorTracker_mock_data.csv"

registros = cargar_datos (ruta) #dato = lista de dicionarios

#dentro de la anterior se verifican los datos

for registro in registros:
    di = registro["ID"]
    for di in range(len(registros)):
        try:
          tiempos,cantidades = filtrar_por_participante(registro, di)
        except TypeError as e:
            print (e)
        except ValueError as e:
            print(e)
try:        
    resultado_tiempo_total = calcular_tiempo_total(tiempos)
    resultado_uso_promedio = calcular_promedio_uso(cantidades)
except IndexError as e:
    print(e)


print(f"su tiempo total es de : {resultado_tiempo_total} y su cantidad promedio es de: {resultado_uso_promedio} ")

    
# sabemos que hay un error en el valor de registros, todo el codigo esta hecho en base a que registros sea una lista de diccionarios
# pero ahora carga de datos tiene que ser un diccionario de diccionarios?
# eso es lo que entendimos de las correcciones y somos concientes de que el codigo sigue con errores especificamente de ese tipo, mas no sabemos como solucionarlos.


