//
// Created by NV7150 on 2020/08/22.
//
#include "Protocols.h"

ProtocolState getProtocolState(byte protocol, byte received){
    if(received == protocol){
        return CORRECT;
    }

    if(
            protocol == PROTOCOL_IMPACT
            || protocol == PROTOCOL_WATER
            || protocol == PROTOCOL_ELSE
            ){
        return INCORRECT;
    }
    return OTHER;
}