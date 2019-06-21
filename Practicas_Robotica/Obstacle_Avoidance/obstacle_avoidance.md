# Obstacle Avoidance Formula 1

## Objetivo de la Práctica

El objetivo de esta práctica es completar el circuito de Fórmula 1 evitando los obstáculos
que se encontrarán en la trayectoria de nuestro coche.<br>
Para ello, se requiere la implementación del algoritmo de Navegación Local **VFF**, el cual
se detalla más adelante.

![Imagen](https://github.com/TheRoboticsClub/2018-colab-FernandoGonzalez/blob/master/docs/obstacle_avoidance.png)

## Hardaware

### Sensores:

El sensor del que disponemos para llevar a cabo este ejercicio es un sensor láser tipo *Lidar*
que toma medidas de distancia entre 0 y 180 grados por delante del robot. De este sensor nos serviremos
para localizar los obstáculos.

### Actuadores:
Como actuadores, el robot posee motores, los cuales le permiten moverse de forma diferencial.

## Sofware

En primer lugar, es necesario indicar que para poder llevar a cabo el algoritmo VFF, se utiliza una navegación híbrida, es decir, el API que se nos proporciona nos facilita las coordenadas globales de los subobjetivos que el robot tiene que ir alcanzando. En total se proporcionan 13 subobjetivos que permiten completar el circuito completo.<br><br>
Se trata de un algoritmo iterativo cuya estructura detallo a continuación:

* En primer lugar, obtengo las coordenadas absolutas del robot (x, y, yaw), donde *yaw* hace referencia al ángulo de orientación.

* Obtengo las coordenadas absolutas del próximo subobjetivo.

* Calculo las coordenadas relativas del objetivo (con respecto a mi robot) a partir de las coordenadas absolutas previamente obtenidas.

* Obtengo los datos del sensor. Estos datos se reciben en un array de 180 posiciones ([0, 180)) donde cada posición almacena un valor de distancia.

* Una vez que poseemos las coordenadas relativas del objetivo y los valores del sensor, se aplica el algortimo *VFF*

### Algoritmo VFF:

Se trata de un algoritmo de navegación local que se basa en el cálculo y suma de fuerzas para calcular la dirección y el sentido óptimos para los que el robot debe navegar.

#### Cálculo de la Fuerza Atractiva:

Con las coordenadas X e Y del objetivo, definimos una fuerza, que se compondrá de módulo y fase. Dicho módulo ha de ser constante a partir de cierta distancia con respecto al robot, para que no crezca esta fuerza de manera incontrolada; y directamente proporcional a la distancia para distancias menores al mencionado umbral, es decir, a más distancia, mayor fuerza.

#### Cálculo de la fuerza Repulsiva:

En primer lugar, convertimos cada ángulo de medida de sensor (que se comprende entre 0 y 180 grados) al rango [-90, 90] grados. Esto se consigue restando 90 grados a dicho ángulo. Posteriormente se le suma 180 grados. Esto se hace debido a que queremos uns fuerza repulsiva, por lo que es necesario invertir la fuerza. Una vez que ya sabemos la fase de la fuerza repulsiva, calculamos las coordenadas X e Y haciendo uso de la medición de distancia de la siguiente forma:
```
x = dist * cos(alpha)
y = dist * sin(alpha)
```
Donde *alpha* es la fase de la fuerza repulsiva.<br>
Por último, con estas coordenadas, calculamos el módulo:
```
mod_repulsiva = sqrt((x ** 2.0) + (y ** 2.0))
```
Si este procedimiento lo llevamos a cabo para todas las posiciones del array que contiene los valores del sensor y vamos reescribiendo los valores de la fase y el módulo y sumando las coordenadas, tendremos un sumatorio de todas las fuerzas repulsivas, lo cual era el objetivo.

#### Cálculo de la fuerza Resultante:

Finalmente, una vez calculadas las fuerzas atractiva y repulsiva, es necesario combinarlas para hallar el vector resultante que nos dará la información que necesitamos enviar a los motores para que el movimiento del robot sea óptimo.<br>
En primer lugar,debemos sumar las coordenadas X e Y de las fuerzas atractiva y repulsiva. Estos valores que obtendremos serán las coordenadas de nuestro vector resultante, de manera que:
```
(x_resultante, y_resultante) = (x_atractiva + x_repulsiva, y_atractiva + y_repulsiva)
```
Posteriormente, calculamos el módulo y la fase de este vector de manera análoga a como se hizo previamente con la fuerza repulsiva.<br><br>
**Y aquí finaliza el algoritmo VFF**<br><br>
Ahora sólo es necesario indicar cuáles serian las velocidades lineal y angular que enviaremos a los motores.<br>
* La velocidad lineal será la resta de los módulos de las fuerzas atractiva y repulsiva
* La velocidad angular será la fase del vector resultante

```
v = mod_atractiva - mod_repulsiva
w = phase_resultante
```

## Apoyo Visual

En este [Enlace](https://www.youtube.com/watch?v=5e_4mkwI8yQ&t=2s) podrás ver una demostración de funcionamiento
