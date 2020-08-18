#include "ReceiveManager.h"
#include "Shock.h"
#include "Pins.h"

using namespace Pins;

ReceiveManager* receiveMan;
Shock* shock;

void setup(){
    receiveMan = new ReceiveManager(115200);
    shock = new Shock(&MOTOR_PIN, &SOLENOID_PIN);

    receiveMan->registerReceiver(shock);
}

void loop(){
    receiveMan->process();
    shock->loop();
}
