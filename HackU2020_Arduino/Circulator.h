//
// Created by NV7150 on 2020/08/26.
//

#ifndef HACKU2020_ARDUINO_CIRCULATOR_H
#define HACKU2020_ARDUINO_CIRCULATOR_H

#include "ReceiveBehavior.h"
#include "Pin.h"
using namespace Pins;

class Circulator : public ReceiveBehavior{
public:
    Circulator(const Pin& pin);
    void received(byte b) override;

private:
    int pin;
};


#endif //HACKU2020_ARDUINO_CIRCULATOR_H
