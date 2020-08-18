//
// Created by koichihirachi on 2020/08/18.
//

#include "Water.h"

Water::Water(const Pin *fanPin) : fanPin(fanPin->getPinNumber())
{
    digitalWrite(fanPin, HIGH);
}

void Water::received(byte b)
{
    if (b == this->PROTOCOL)
    {
        manageWater();
    }
    else
    {
        disableWater();
    }
}

void Water::manageWater()
{
    this->isEnable = true;
}

void Water::disableWater()
{
    this->isEnable = false;
}

void Water::switchWater()
{
    switch (fanState)
    {
    case OFF:
        this->fanState = WEAK;
        break;
    case WEAK:
        this->fanState = MIDDLE;
    case MIDDLE:
        this->fanState = HARD;
        break;
    case HARD:
        this->fanState = OFF;
        break;
    }
    digitalWrite(fanPin, LOW);
    delay(10);
    digitalWrite(fanPin, HIGH);
    delay(10);
}

void Water::loop()
{
    if (isEnable)
    {
        while (fanState != defaultPower)
            switchWater();
    }
    else
    {
        while (fanState != OFF)
            switchWater();
    }
}
