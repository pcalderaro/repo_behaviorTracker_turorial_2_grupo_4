#import pandas  #no se si tengo que poner esto aca o no
from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_total
from src.metricas import calcular_promedio_uso
from src.diseño import graficar_metricas
# ruta = "datos/BehaviorTracker_mock_data_error(nuemero).csv"
ruta = "datos/BehaviorTracker_mock_data.csv"


registros = cargar_datos(ruta) #resgistros es un dtaframe sin valores nulos
while True:
    entrada = input("Ingrese el ID del participante que desea filtrar: ")
    try:
        id_buscado = int(entrada)
        break
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")
        
if id_buscado in registros["id_participante"].values:
   participante = registros.loc[registros["id_participante"] == id_buscado]
   
   try:
     tiempos,cantidades = filtrar_por_participante(registros, participante)
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
           graficar_metricas(tiempos, cantidades, id_buscado)
else:
    print(f"El participante con ID {id_buscado} no fue encontrado en los registros.")
    
   
       
 