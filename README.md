# repo_behaviorTracker_turorial_2_grupo_4

El sistema es un trakeo del comportamiento de las personas, relacionado a su uso de aplicaciones.

El codigo lee datos discretos por día, estos son múltiples registros por participante de múltiples aplicaciones por día. Luego transforma cada linea en un registro (diccionario)y alacena los datos en la memoria.
por ultimo organiza los datos a medir de los participantes (tiempo y cantidad de uso) y calcula las metricas: tiempo total de uso y cantidad promedio.


este proyecto esta contruido por: Pilar Calderaro, Valentina Entrala, Camila Iglesias Y Uma Rodriguez Videla

Objetivo
Desarrollar un sistema que permita:
-  leer y estructurar datos de uso digital
-  representar comportamiento a lo largo del tiempo
-  Calcular métricas básicas de uso

Estrucutura de los datos

-  id_participante: identificador del participante
-  fecha: día de registro
-  app: nombre de la aplicación
-  cantidad_uso: cantidad de veces que se abrió la app
-  tiempo_uso: tiempo total de uso

Métricas a calcular
1.  Tiempo total de uso → intensidad de uso
2.  Promedio de uso → comportamiento típico

Implementacion de objjetos de la funcion cargar_datos()
  Se define una clase Registro para representar cada linea del archivo. 
  Los atributos son : id_participante, fecha, app, cantidad_uso, tiempo_uso. 
  Los metodos son: __init__ que es el que incializa los obejtos y
