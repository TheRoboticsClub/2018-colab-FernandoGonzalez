/*
 * To send the Joysticks information by radiofrequency
 */
#include <VirtualWire.h>

const int Antenna = 2;
const int Vy = 0;
const int Vx = 1;

int dato[2];

void setup() {
  Serial.begin(9600);
  
  vw_setup(2000); //Speed: Bits per second
  vw_set_tx_pin(Antenna); //Output for the RF 
}

void loop() {
  
    //Read the Joysticks data
    dato[0] = map(analogRead(Vx), 0, 1024, 0, 255);
    dato[1] = map(analogRead(Vy), 0, 1024, 0, 255);
    //Print it by screen
    Serial.println(dato[0]);
    Serial.println(dato[1]);
    Serial.println("----");
    //Send them by the antenna
    vw_send((uint8_t*)dato, 3);
    vw_wait_tx();
    
    delay(50);
}
