# Follow Line Turtlebot

## Objetivo de la Práctica
El objetivo de esta práctica es conseguir que el kobuki se mueva siguiendo una línea blanca pintada en el suelo hasta completar el circuito

![Imagen](https://www.turtlebot.com/assets/images/turtlebot2e.png)

## Hardware

El hardware del robot utilizado para esta práctica se clasifica de la siguiente manera:

### Sensores:

El sensor se trata de una cámara RGBD mediante la cual se podŕa detectar la línea blanca.

### Actuadores:

Como actuadores, en este caso disponemos de los motores que permiten moverse al kobuki

## Software

El software del que consta este ejercicio no es más que una adaptación del código utilizado para la plataforma simulada.

Se ha utilizado un algoritmo reactivo de **control proporcional** para conseguir que el robot corrija su trayectoria de manera que la línea blanca siempre se encuentre en el centro de la imagen captada por la cámara.

El cambio principal que ha sufrido han sido los valores HSV utilizados para realizar el filtro de la imagen, debido a que el
color es diferente y también a que en un entorno real, los colores no son constantes sino que sufren variaciones debido a infinidad de factores físicos que en una simulación no están presentes, así como brillos, sombras, etc...

Es por esta razón que además de calibrar de la manera más rigurosa posible el filtro (de manera experimental), para aumentar la robustez del comportamiento del robot ha sido necesario realizar dos operaciones sobre la imagen una vez filtrada. Estas dos operaciones son *dilatar* y *erosionar*. Éstos son conceptos que explicaré a continuación:

* **Dilatar:** Partimos de una imagen filtrada, es decir, una matriz de unos y ceros. El proceso de dilatació consiste en crear una nueva matriz cuadrada de las dimensiones que creamos oportunas. Esta matriz, denominada *kernel* se desliza por la matriz que forma la imagen y si al menos un pixel de los que caen dentro de ese kernel es un 1, todos se convertirán en 1. En caso contrario, seguirán siendo 0.

* **Erosionar:** Es la operación contraria a la dilatación. Para conseguir un 1, todos los elementos que caigan dentro del kernel tendrán que estar a 1. Y lo mismo para el 0.

Con estas dos operaciones ppodemos ser capaces de eliminar el ruido de forma significativa. 

Para poder aplicar ambas operaciones simultáneamente se hace uno del método que OpenCV nos proporciona:
```
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
```

## Apoyo Visual

En el siguiente [Enlace](https://www.youtube.com/watch?v=uEgDbSsNcSA) se encuentra el vídeo del Turtlebot en funcionamiento
