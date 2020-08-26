//
// Created by NV7150 on 2020/08/18.
//

#ifndef HACKU2020_ARDUINO_PINS_H
#define HACKU2020_ARDUINO_PINS_H

#include "Pin.h"

namespace Pins
{
    const Pin MOTOR_PIN(8, DIG_OUT);
    const Pin SOLENOID_PIN(13, DIG_OUT);
    const Pin FAN_PIN(7, DIG_OUT);

    const Pin LED_RED_PIN(4, DIG_OUT);
    const Pin LED_BLUE_PIN(5, DIG_OUT);
    const Pin LED_GREEN_PIN(6, DIG_OUT);

    const Pin MOTOR_PUNCH_PIN(3, ANALOG);

    const Pin CIRCULATOR_PIN(2, DIG_OUT);
} // namespace Pins

#endif //HACKU2020_ARDUINO_PINS_H
