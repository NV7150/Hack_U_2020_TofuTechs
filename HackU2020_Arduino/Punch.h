//
// Created by NV7150 on 2020/08/22.
//

#ifndef HACKU2020_ARDUINO_PUNCH_H
#define HACKU2020_ARDUINO_PUNCH_H

#include <Arduino.h>
#include <Servo.h>

#include "ReceiveBehavior.h"
#include "Pin.h"

using namespace Pins;

class Punch : public ReceiveBehavior{
public:
    Punch(Pin& servoPin);

    void received(byte b) override;

    void loop();

private:
    const int DEFAULT_ANGLE = 0;
    const int PUNCH_ANGLE = 180;
    const int PUNCH_INTERVAL = 250;

    Servo* servo;

    unsigned long lastPunch = 0;
    bool isEnable = false;
    bool isPunching = false;
};


#endif //HACKU2020_ARDUINO_PUNCH_H
