//
// Created by NV7150 on 2020/08/22.
//

#ifndef HACKU2020_ARDUINO_LIGHTS_H
#define HACKU2020_ARDUINO_LIGHTS_H

#include "ReceiveBehavior.h"
#include "Pin.h"

using namespace  Pins;

class Lights : public ReceiveBehavior{
public:
    Lights(const Pin& redPin, const Pin& bluePin, const Pin& greenPin);

    void received(byte b) override;

    void loop();

private:
    const int LIGHT_INTERVAL = 500;

    int redPin;
    int bluePin;
    int greenPin;

    bool isEnable = false;
    bool isTurningOn = false;
    unsigned long lastTurnOn;

    void turnOn();
    void turnOff();
};


#endif //HACKU2020_ARDUINO_LIGHTS_H
