//
// Created by NV7150 on 2019/11/15.
//

#ifndef PINS_PIN_H
#define PINS_PIN_H


#include <Arduino.h>
namespace Pins {

    //PINのモード
    enum PinOption {
        //デジタル入力
        DIG_IN,
        //デジタル出力
        DIG_OUT,
        //デジタル入力（プルアップ）
        DIG_IN_PULLUP,
        //アナログ入出力
        ANALOG
    };

    using Pins::PinOption;

    //Arduinoのいずれかのピンを示すクラス
    class Pin {
    public:
        //コンストラクタ
        Pin(uint8_t pinNumber, PinOption pinOption);
        //ピン番号を取得
        uint8_t getPinNumber() const;

    private:
        //ピン番号
        const uint8_t pinNumber;
        //ピンのモード
        PinOption pinOption;
    };
}



#endif //PINS_PIN_H
