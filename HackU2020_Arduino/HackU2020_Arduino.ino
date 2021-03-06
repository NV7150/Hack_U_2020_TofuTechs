#include "ReceiveManager.h"
#include "Shock.h"
#include "Water.h"
#include "Mist.h"
#include "Pins.h"
#include "Lights.h"
#include "Punch.h"
#include "Circulator.h"

using namespace Pins;

/*
 * Usage
 * Shock.hを参考に，ReceiveBehaviorを継承したクラスを作成
 * 注意！継承する時は「クラス名 : public ReceiveBehavior」として，publicを必ずつける！
 * received(byte)メソッドに，なんらかのシリアルを受け取った際の処理を作成
 * （受け取った信号が自分にむけたものかの判断も込みで）
 * 以下を参考にしてreceiveMan->registerReceiverを使ってreceiveManにクラスを登録
 * あとはだいたいやってくれる
 *
 * loopごとにしたい処理月たらShockみたいな感じにpublicメソッド実装してね
 * */

ReceiveManager *receiveMan;
Shock *shock;
Mist *mist;
Lights* lights;
Punch* punch;
Circulator* circulator;

void setup(){
    Serial.begin(115200);
    receiveMan = new ReceiveManager(5);
    shock = new Shock(&MOTOR_PIN, &SOLENOID_PIN);
    mist = new Mist(&FAN_PIN);
    lights = new Lights(LED_RED_PIN, LED_BLUE_PIN, LED_GREEN_PIN);
    punch = new Punch(MOTOR_PUNCH_PIN);
    circulator = new Circulator(CIRCULATOR_PIN);

    receiveMan->registerReceiver(shock);
    receiveMan->registerReceiver(mist);
    receiveMan->registerReceiver(lights);
    receiveMan->registerReceiver(punch);
    receiveMan->registerReceiver(circulator);
}

void loop(){
    receiveMan->process();
    shock->loop();
    mist->loop();
    lights->loop();
}
