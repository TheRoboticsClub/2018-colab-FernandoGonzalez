# Follow Line Turtlebot

## Objetivo de la Práctica
El objetivo de esta práctica es conseguir que el kobuki se mueva siguiendo una línea blanca pintada en el suelo hasta completar el circuito

## Hardware

El hardware del robot utilizado para esta práctica se clasifica de la siguiente manera:

### Sensores:

El sensor se trata de una cámara RGBD mediante la cual se podŕa detectar la línea blanca.

### Actuadores:

Como actuadores, en este caso disponemos de los motores que permiten moverse al kobuki

## Software

El software del que consta este ejercicio no es más que una adaptación del código utilizado para la plataforma simulada.

El cambio principal que ha sufrido han sido los valores HSV utilizados para realizar el filtro de la imagen, debido a que el
color es diferente y también a que en un entorno real, los colores no son constantes sino que sufren variaciones debido a infinidad de factores físicos que en una simulación no están presentes así como brillos, sombras, eetc...
