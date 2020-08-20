//
// Created by NV7150 on 2020/08/20.
//

#ifndef HACKU2020_ARDUINO_MIST_H
#define HACKU2020_ARDUINO_MIST_H

#include "ReceiveBehavior.h"
#include "Pin.h"
using namespace Pins;

enum MistState{
    MISTING,
    NONE
};


class Mist : public ReceiveBehavior{
public:
    Mist(const Pin* pin);

    void received(byte b) override;
    void loop();

private:
    const int PUSHING_TIME = 2000;

    MistState currState = NONE;
    MistState processingState = NONE;
    bool processEnabled = false;
    MistState requireState = NONE;
    unsigned long pushStart = 0;
    int mistPin;

};


#endif //HACKU2020_ARDUINO_MIST_H
