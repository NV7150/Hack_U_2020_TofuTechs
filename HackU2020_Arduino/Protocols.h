//
// Created by NV7150 on 2020/08/18.
//

#ifndef HACKU2020_ARDUINO_PROTOCOLS_H
#define HACKU2020_ARDUINO_PROTOCOLS_H

#include <Arduino.h>

const byte PROTOCOL_IMPACT = (byte)('i');
const byte PROTOCOL_WATER = (byte)('w');
const byte PROTOCOL_ELSE = (byte)('e');

enum ProtocolState{
    CORRECT,
    INCORRECT,
    OTHER
};

ProtocolState getProtocolState(byte protocol, byte received);

#endif //HACKU2020_ARDUINO_PROTOCOLS_H
