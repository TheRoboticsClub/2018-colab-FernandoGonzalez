# Ejercicio Gato-Ratón

## Objetivo de la Práctica
El objetivo de esta práctica es conseguir que el drone gato (negro) siga al drone rojo (gato) durante dos minutos. Esto se lleva a cabo mediante la plataforma web de JdeRobot Academy, en la cual se encuentra una simulación del entorno con Gazebo.

![Imagen](https://github.com/TheRoboticsClub/2018-colab-FernandoGonzalez/blob/master/docs/drone_cat_mouse.png)

## Hardware
El hardware disponible en este drone se desglosa de la siguiente manera:

### Sensores:
El drone dispone de dos cámaras. Una de ellas situada en la parte frontal y mirando hacia el frente y la otra que se sitúa en la zona ventral del drone y que apunta hacia el suelo. Sin embargo, para la realización del ejercicio sólo se usa la cámara frontal.

### Actuadores:
Como actuadores se encuentran los motores de las hélices, los cuales proporcionan al drone la movilidad.

## Software
El software se basa en un sistema reactivo implementando un control proporcional. Por ser reactivo, todo el programa se ejecuta en bucle infinito. A continuación procedo a analizar las dos partes más importantes de la algoritmia:

**1. Análisis de la Imagen:** En cada iteración del bucle, se captura una imagen de la cámara frontal y se le aplica un filtro de color rojo (color del drone ratón) para posteriormente calcular su centro y su área.

**2. Toma de Decisiones:** Con el valor del centro ya calculado, podremos corregir la posición del drone en función del error que presente dicho centro con el centro real de la imagen tanto en *x* como en *y*. De esta forma podremos comandar a nuestro drone que gira a la derecha o izquierda y que suba o baje. 

En relación con acercarse o alejarse del drone ratón, esto lo haremos teniendo en cuenta el área también calculada previamente. Si el área es muy grande querrá decir que el ratón está demasiado cerca, y si es más pequeña querrá decir que se encuentra más lejos. De esta manera podemos controlar el avance o retroceso del drone gato.

## Apoyo Visual:
En el siguiente [enlace](https://www.youtube.com/watch?v=uiK6WXPU_VQ) se encuentra un vídeo de la realización del ejercicio, en el cual se obtiene una puntuación de 761 puntos.
