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
    Punch(const Pin& motorPin);

    void received(byte b) override;

private:
    const int SPEED = 255;

    int pin;
};


#endif //HACKU2020_ARDUINO_PUNCH_H
