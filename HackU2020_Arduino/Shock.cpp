//
// Created by NV7150 on 2020/08/18.
//

#include "Shock.h"
#include "Protocols.h"

Shock::Shock(const Pin *motorPin,const Pin *solenoidPin)
: motorPin(motorPin->getPinNumber()), solenoidPin(solenoidPin->getPinNumber()){

}

void Shock::received(byte b) {
    if(b == PROTOCOL_IMPACT){
        manageShock();
    }else if(b == PROTOCOL_ELSE){
        disableShock();
    }
}

void Shock::manageShock() {
    this->isEnable = true;
}

void Shock::disableShock() {
    this->isEnable = false;
}

//void debug(){
//    tone(12, 450, 1000);
//    delay(1000);
//}

void Shock::loop() {
    if(this->isEnable) {
        digitalWrite(motorPin, HIGH);

        this->solenoidState = (solenoidState == HIGH) ? LOW : HIGH;
        digitalWrite(solenoidPin, solenoidState);

//        debug();
    }else{
        digitalWrite(motorPin, LOW);

        this->solenoidState = LOW;
        digitalWrite(solenoidPin, solenoidState);

    }
}
