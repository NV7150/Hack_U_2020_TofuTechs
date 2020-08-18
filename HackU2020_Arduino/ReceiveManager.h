//
// Created by NV7150 on 2020/08/18.
//

#ifndef HACKU2020_ARDUINO_RECEIVEMANAGER_H
#define HACKU2020_ARDUINO_RECEIVEMANAGER_H

#include <Arduino.h>
#include <Vector.h>

#include "ReceiveBehavior.h"

class ReceiveManager {
public:
    //コンストラクタ
    ReceiveManager(int baudRate);
    //ReceiveBehaviorを継承したクラスのインスタンスを登録
    void registerReceiver(ReceiveBehavior* receiveBehavior);
    //loopごとに呼び出し
    void process();

private:
    Vector<ReceiveBehavior*>* receivers;
};


#endif //HACKU2020_ARDUINO_RECEIVEMANAGER_H
