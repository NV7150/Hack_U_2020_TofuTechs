//
// Created by koichihirachi on 2020/08/18.
//

#ifndef HACKU2020_ARDUINO_WATER_H
#define HACKU2020_ARDUINO_WATER_H

#include <Arduino.h>

#include "ReceiveBehavior.h"
#include "Pin.h"

using namespace Pins;

class Water : public ReceiveBehavior
{
    typedef enum
    {
        OFF,
        WEAK,
        MIDDLE,
        HARD
    } FanState;

public:
    Water(const Pin *fanPin);
    void received(byte b) override;
    void loop();

private:
    const byte PROTOCOL = (byte)('w');

    int fanPin;

    bool isEnable = false;

    FanState fanState = WEAK; //電源をつけたとき

    FanState defaultPower = HARD; //扇風機の速さ

    void manageWater();
    void disableWater();
    void switchWater();
};

#endif //HACKU2020_ARDUINO_WATER_H
