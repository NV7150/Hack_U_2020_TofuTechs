//
// Created by NV7150 on 2020/08/18.
//

#include "Shock.h"

Shock::Shock(const Pin *motorPin,const Pin *solenoidPin)
: motorPin(motorPin->getPinNumber()), solenoidPin(solenoidPin->getPinNumber()){

}

void Shock::received(byte b) {
    if(b == this->PROTOCOL){
        manageShock();
    }else{
        disableShock();
    }
}

void Shock::manageShock() {
    this->isEnable = true;
}

void Shock::disableShock() {
    this->isEnable = false;
}

void Shock::loop() {
    if(this->isEnable) {
        digitalWrite(motorPin, HIGH);

        this->solenoidState = (solenoidState == HIGH) ? LOW : HIGH;
        digitalWrite(solenoidPin, solenoidState);
    }else{
        digitalWrite(motorPin, LOW);

        this->solenoidState = LOW;
        digitalWrite(solenoidPin, solenoidState);

    }
}
