cmake_minimum_required(VERSION 3.12)
project(HackU2020_Arduino)

set(CMAKE_CXX_STANDARD 14)

include_directories(/Applications/Arduino.app/Contents/Java/hardware/arduino/avr/cores/arduino)
include_directories(/Applications/Arduino.app/hardware/arduino/avr/variants/standard)
include_directories(/Applications/Arduino.app/hardware/tools/avr/avr/include)
include_directories(/Applications/Arduino.app/hardware/tools/avr/lib/gcc/avr/4.9.2/include)
include_directories(/Applications/Arduino.app/Contents/Java/libraries/WiFi/src)
include_directories(~/Documents/Arduino/hardware/espressif/esp32/tools/sdk/include/esp32)
include_directories(~/Documents/Arduino/hardware/espressif/esp32/libraries/WiFi/src/)
include_directories(~/Documents/Arduino/hardware/espressif/esp32/libraries/BLE/src/)
include_directories(~/Documents/Arduino/libraries)
include_directories(~/Documents/Arduino/hardware/espressif/esp32/libraries)
include_directories(/Applications/Arduino.app/Contents/Java/libraries/Servo/src)
include_directories(~/Documents/Arduino/libraries/VL53L0X)
include_directories(/Applications/Arduino.app/Contents/Resources)
include_directories(/Applications/Arduino.app/Contents/Java/hardware/arduino/avr/libraries/Wire/src/)
include_directories(~/Documents/Arduino/libraries/Vector/src)
include_directories(~/Documents/Arduino/libraries/Adafruit_NeoPixel)

add_executable(HackU2020_Arduino
        HackU2020_Arduino.ino
        ReceiveManager.cpp ReceiveManager.h
        ReceiveBehavior.h
        Shock.cpp Shock.h
        Pin.cpp Pin.h Pins.h Protocols.h
        Water.h Water.cpp Mist.cpp Mist.h Lights.cpp Lights.h Protocols.cpp Punch.cpp Punch.h Circulator.cpp Circulator.h)