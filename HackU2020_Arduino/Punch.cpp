//
// Created by NV7150 on 2020/08/22.
//

#include "Punch.h"
#include "Protocols.h"

Punch::Punch(Pin &motorPin) : pin(motorPin.getPinNumber()){

}

void Punch::received(byte b) {
    auto state = getProtocolState(PROTOCOL_IMPACT, b);
    if(state == CORRECT){
        analogWrite(pin, SPEED);
    }else if(state == INCORRECT){
        analogWrite(pin, 0);
    }
}
