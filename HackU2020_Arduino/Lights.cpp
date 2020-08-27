//
// Created by NV7150 on 2020/08/22.
//

#include <Arduino.h>
#include "Lights.h"
#include "Protocols.h"

Lights::Lights(const Pin& redPin, const Pin& bluePin, const Pin& greenPin) :
redPin(redPin.getPinNumber())
, bluePin(bluePin.getPinNumber())
, greenPin(greenPin.getPinNumber()) {}

void Lights::received(byte b) {
    auto protocolState = getProtocolState(PROTOCOL_IMPACT, b);
    if(protocolState == CORRECT){
        isEnable = true;
    }else if(protocolState == INCORRECT){
        isEnable = false;
    }
}

void Lights::loop() {
    if(isEnable){
        if(millis() - lastTurnOn > LIGHT_INTERVAL){
            (isTurningOn) ? turnOff() : turnOn();
            lastTurnOn = millis();
        }
    }else{
        turnOff();
    }
}

void Lights::turnOn() {
    digitalWrite(redPin, HIGH);
    digitalWrite(bluePin, HIGH);
    digitalWrite(greenPin, HIGH);
    isTurningOn = true;
}

void Lights::turnOff() {
    digitalWrite(redPin, LOW);
    digitalWrite(bluePin, LOW);
    digitalWrite(greenPin, LOW);
    isTurningOn = false;
}
