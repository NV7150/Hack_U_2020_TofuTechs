//
// Created by NV7150 on 2020/08/18.
//

#ifndef HACKU2020_ARDUINO_SHOCK_H
#define HACKU2020_ARDUINO_SHOCK_H

#include <Arduino.h>

#include "ReceiveBehavior.h"
#include "Pin.h"

using namespace Pins;

class Shock : public ReceiveBehavior{
public:
    Shock(const Pin* motorPin,const Pin* solenoidPin);
    void received(byte b) override;
    void loop();

private:
    int motorPin;
    int solenoidPin;

    bool isEnable = false;
    int solenoidState = LOW;

    void manageShock();
    void disableShock();
};


#endif //HACKU2020_ARDUINO_SHOCK_H
