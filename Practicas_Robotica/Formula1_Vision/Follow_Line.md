# Sigue Líneas Fórmula 1

## Objetivo de la Practica
El objetivo de esta práctica es conseguir que el coche de Fórmula 1 sea capaz de completar
el circuito en el menor tiempo posible siguiendo la línea roja pintada sobre el circuito.
Esta práctica se llevará a cabo utilizando la plataforma web de JdeRobot Academy, la cual contiene la simulación.

![Imagen](https://github.com/TheRoboticsClub/2018-colab-FernandoGonzalez/blob/master/docs/jderobot_academy.png)

## Hardware
El hardware del robot utilizado para este ejercicio se puede desglosar de la siguiente manera:

### Sensores:
El único sensor presente en este robot es una cámara situada en su parte frontal.

### Actuadores:
Como actuadores, tenemos los motores del robot, los cuales nos permites tener un control basado en velocidad
tanto lineal como angular

## Software
El software de este robot se basa en un sistema reactivo con un control proporcional.
Al tratarse de un sistema reactivo, el programa principal de un bucle infinito cuya estructura básica consta de las
siguientes fases:

**1. Análisis de la Imagen:** Se realiza con funciones básicas de OpenCV

**2. Toma de Decisión:** En función de la información extraída de la imagen previamente analizada, se toma una decisión
que se traduce en un cierto comportamiento del robot. A continuación explico más detalladamente cómo se lleva a cabo
esta toma de decisiones y sus implicaciones.

### Algoritmo de Toma de Decisiones:
En primer lugar, la imagen se hace pasar por un filtro de color rojo (color de la línea) y posteriormente se calcula su
centro. El pseudocódigo expuesto a continuación muestra la lógica decisoria:
```
while(True):
    img = imagen_sin_procesar
    mask = imagen_filtrada
    c = centro(mask)

    if(estoySobreLinea(mask)):
        avanzar(mask)
    elif(desviadoIzquierda(x)):
        girarDerecha(x)
    elif(desviadoDerecha(x)):
        girarIzquierda(x)
```
* *Nota:* Las sentencias ```img = imagen_sin_procesar``` y ```mask = imagen_filtrada``` se llevan a cavo utilizando la librería **cv2** (librería de OpenCV en python).

Como podemos observar, las funciones *girarDerecha* y *girarIzquierda* reciben como parámetro el centro de masas del color
rojo. Esto se debe a que las velocidades angulares y lineales que se les ordena a los motores son proporcionales al error
existente. Este error no es más que la diferencia entre en centro del frame y el centro de masas del color filtrado. De
esta forma, el coche puede encontrarse desviado a la izquierda o a la derecha (esto se encargan de evaluarlo las funciones *desviadoIzquierda* y *desviadoDerecha*).

Además, dentro de la implementación de la función *avanzar* se comtemplan los casos de que el robot se encuentre sobre
una línea recta larga o esté inmerso en una curva, manejando así distintas velocidades.

## Apoyo Visual
En el siguiente [Enlace](https://www.youtube.com/watch?v=B0__VtEqL5w&t=58s) se encuentra el vídeo del coche en funcionamiento.
