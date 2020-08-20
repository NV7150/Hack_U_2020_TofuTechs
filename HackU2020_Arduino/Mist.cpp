//
// Created by NV7150 on 2020/08/20.
//

#include "Mist.h"
#include "Protocols.h"

Mist::Mist(const Pin* mistPin) : mistPin(mistPin->getPinNumber()) {}

void Mist::received(byte b) {
    if(b == PROTOCOL_WATER){
        requireState = MISTING;
    }else if(b == PROTOCOL_ELSE || b == PROTOCOL_IMPACT){
        requireState = NONE;
    }
}


void Mist::loop() {
    if(processingState != currState){
        if(!processEnabled){
            pushStart = millis();
            digitalWrite(mistPin, HIGH);
        }
        if(millis() - pushStart > PUSHING_TIME){
            digitalWrite(mistPin, LOW);
            processEnabled = false;
            currState = processingState;
        }
    }

    if(!processEnabled && processEnabled != requireState){
        processingState = requireState;
    }
}
