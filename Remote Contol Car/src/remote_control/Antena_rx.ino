/*
 * Receive commands by remote control and it decide the turn angle of front wheels axis
 * and the back wheels polarity
 */

#include <VirtualWire.h>

void setup()
{
    Serial.begin(9600);
    Serial.println("setup");

    //Se inicializa el RF
    vw_setup(2000);  //velocidad: Bits per segundo
    vw_set_rx_pin(2);
    vw_rx_start();
    
    pinMode(13, OUTPUT);
    pinMode(7, OUTPUT);
    digitalWrite(13, false);
    digitalWrite(7, false);
}

int vx;
int vy;

int movement_robot[2]; //Array that defines the robot movement

void loop()
{
    uint8_t data[VW_MAX_MESSAGE_LEN];
    uint8_t dataleng = VW_MAX_MESSAGE_LEN;
    
    if (vw_get_message(data,&dataleng)){

        vx = data[0]; //Axis x information (wheels orientation)
        vy = data[2]; //Axis y information (wheels polarity)

    }

    movement_robot[0] = map(vx, 0, 250, 45, 135); //Save the degrees that will move the servomotor
    
    if(vy > 130){
      movement_robot[1] = 1; // 1 if motors have to go forward, and -1 if motors have to go backward
    }else if(vy < 120){
      movement_robot[1] = -1;
       
    }else{
      movement_robot[1] = 0;
    }

    Serial.println(movement_robot[0]);
    Serial.println(movement_robot[1]);
    Serial.println("----");
    
    delay(200);
}
