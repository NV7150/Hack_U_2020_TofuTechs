//
// Created by NV7150 on 2020/08/20.
//

#include "Mist.h"
#include "Protocols.h"

Mist::Mist(const Pin* mistPin) : mistPin(mistPin->getPinNumber()) {}

void Mist::received(byte b) {
    auto state = getProtocolState(PROTOCOL_WATER, b);
    if(state == CORRECT){
        requireState = MISTING;
    }else if(state == INCORRECT){
        requireState = NONE;
    }
}


void Mist::loop() {
    if(processingState != currState){
        if(!processEnabled){
            pushStart = millis();
            digitalWrite(mistPin, HIGH);
            processEnabled = true;
        }
        if(millis() - pushStart > PUSHING_TIME){
            digitalWrite(mistPin, LOW);
            processEnabled = false;
            currState = processingState;
        }
    }

    if(!processEnabled && processingState != requireState){
        processingState = requireState;
    }
}
