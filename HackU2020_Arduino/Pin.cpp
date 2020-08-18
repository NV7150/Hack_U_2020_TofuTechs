//
// Created by NV7150 on 2019/11/15.
//

#include "Pin.h"
using Pins::Pin;
using Pins::PinOption;

//初期化時に引数に応じてpinModeを設定
Pin::Pin(uint8_t pinNumber, PinOption pinOption) : pinNumber(pinNumber), pinOption(pinOption) {
    //アナログピンならpinModeの必要なし
    if(ANALOG == pinOption){
        return;
    }

    //実際のpinMode引数の値
    uint8_t trueOption;

    //INPUT, OUTPUT, INPUT_PULLUPの値をpinOption応じて設定
    switch (pinOption){
        case DIG_IN:
            trueOption = INPUT;
            break;

        case DIG_OUT:
            trueOption = OUTPUT;
            break;

        case DIG_IN_PULLUP:
            trueOption = INPUT_PULLUP;
            break;

        default:
            return;
    }

    //pinModeに設定
    pinMode(pinNumber, trueOption);
}

uint8_t Pin::getPinNumber() const {
    return pinNumber;
}
