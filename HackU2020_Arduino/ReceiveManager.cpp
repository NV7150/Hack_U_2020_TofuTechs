//
// Created by NV7150 on 2020/08/18.
//

#include "ReceiveManager.h"

extern HardwareSerial Serial;

ReceiveManager::ReceiveManager(int baudRate) {
    Serial.begin(baudRate);
    this->receivers = new Vector<ReceiveBehavior*>();
}

void ReceiveManager::registerReceiver(ReceiveBehavior *receiveBehavior) {
    receivers->push_back(receiveBehavior);
}

void ReceiveManager::process() {
    if(Serial.available()){
        byte data = Serial.read();
        for(int i = 0; i < receivers->size(); i++){
            receivers->at(i)->received(data);
        }
    }
}
