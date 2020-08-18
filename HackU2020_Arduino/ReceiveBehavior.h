//
// Created by NV7150 on 2020/08/18.
//

#ifndef HACKU2020_ARDUINO_RECEIVEBEHAVIOR_H
#define HACKU2020_ARDUINO_RECEIVEBEHAVIOR_H

#include <Arduino.h>

class ReceiveBehavior {
public:
    //シリアルに何か入った場合，receivedが呼び出される
    virtual void received(byte b) = 0;
};


#endif //HACKU2020_ARDUINO_RECEIVEBEHAVIOR_H
