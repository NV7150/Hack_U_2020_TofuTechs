//
// Created by NV7150 on 2020/08/18.
//

#include "ReceiveManager.h"

extern HardwareSerial Serial;

ReceiveManager::ReceiveManager(int storageSize)
: receivers(new Vector<ReceiveBehavior*>), storageIncrease(storageSize){
    auto** arr = new ReceiveBehavior*[storageSize];
    receivers->setStorage(arr, storageSize, 0);
}

void ReceiveManager::registerReceiver(ReceiveBehavior *receiveBehavior) {
    storageCount++;
    if(storageCount > receivers->max_size()){
        //ストレージ増量
        auto** arr = new ReceiveBehavior*[storageCount + storageIncrease];
        for(int i = 0; i < receivers->size(); i++){
            arr[i] = receivers->at(i);
        }

        receivers->setStorage(arr, storageCount + storageIncrease, receivers->size());
    }
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
