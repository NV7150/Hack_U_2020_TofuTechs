//
// Created by NV7150 on 2020/08/22.
//

#include "Punch.h"
#include "Protocols.h"

Punch::Punch(Pin &servoPin) : servo(new Servo){
    servo->attach(servoPin.getPinNumber());
    servo->write(0);
}

void Punch::received(byte b) {
    auto state = getProtocolState(PROTOCOL_IMPACT, b);
    if(state == CORRECT){
        isEnable = true;
    }else if(state == INCORRECT){
        isEnable = false;
    }
}

void Punch::loop() {
    if(isEnable){
        if(millis() - lastPunch > PUNCH_INTERVAL){
            auto angle = (isPunching) ? DEFAULT_ANGLE : PUNCH_ANGLE;
            servo->write(angle);
            isPunching = !isPunching;
            lastPunch = millis();
        }
    }else{
        if(isPunching){
            servo->write(DEFAULT_ANGLE);
            isPunching = false;
        }
    }
}
