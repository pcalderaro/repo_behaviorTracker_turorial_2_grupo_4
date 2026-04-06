from scr.carga_datos import cargar_datos
from scr.procesamiento_datos import filtrar_por_participante
from scr.metricas import calcular_tiempo_total
from scr.metricas import calcular_promedio_uso

registros = cargar_datos ("archivo.csv") #dato = lista de listas

#dentro de la anterior se verifican los datos

for registro in registros:
    di = registro["ID"]
    for di in range(len(registros)):
        tiempos,cantidades = filtrar_por_participante(registro, di)
        
resultado_tiempo_total = calcular_tiempo_total(tiempos)
resultado_uso_promedio = calcular_promedio_uso(cantidades)

print(f"su tiempo total es de : {resultado_tiempo_total} y su cantidad promedio es de: {resultado_uso_promedio} ")

    
    


