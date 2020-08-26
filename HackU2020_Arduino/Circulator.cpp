//
// Created by NV7150 on 2020/08/26.
//

#include <Arduino.h>

#include "Circulator.h"
#include "Protocols.h"


Circulator::Circulator(const Pin &pin): pin(pin.getPinNumber()) {

}

void Circulator::received(byte b) {
    auto com = getProtocolState(PROTOCOL_IMPACT, b);
    if(com == CORRECT){
        digitalWrite(pin, HIGH);
    }else if (com == INCORRECT){
        digitalWrite(pin, LOW);
    }
}
