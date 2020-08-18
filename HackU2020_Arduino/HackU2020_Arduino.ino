#include "ReceiveManager.h"
#include "Shock.h"
#include "Water.h"
#include "Pins.h"

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
Water *water;

void setup()
{
    Serial.begin(115200);
    receiveMan = new ReceiveManager(1);
    shock = new Shock(&MOTOR_PIN, &SOLENOID_PIN);
    water = new Water(&FAN_PIN);

    receiveMan->registerReceiver(shock);
}

void loop()
{
    receiveMan->process();
    shock->loop();
    water->loop();
}
