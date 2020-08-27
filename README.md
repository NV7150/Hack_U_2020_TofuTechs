# ムービング座布団
 Open Hack U 2020 Online Vol.1[1]でチーム「ご注文は豆腐職人ですか？」が作成した作品です。

# 作品説明
 入力された動画音声をAudiosetとTensorflow/Kerasで作成した音声分類モデルに通し，動画のシーンに合わせた4D体験を提供します。
 リポジストリにアップロードされているプログラムはこちらの開発用のため使用できませんが，副製作物としてオリジナルムービング座布団の雛形システムをリリースしています。

# オリジナルムービング座布団（Release v0.1α）
## 同梱物
### ルート
* main: アプリケーション本体
### Assetディレクトリ
* VGGish[2]の音声特徴量抽出モデル
* Audioset[3]を用いて作った音声分類モデル
* 作業用のwav２種類
## 使い方
### ハード作成編
#### 作成に必要なもの
* マイコンボード(Arduinoでのみ動作確認済み)
* PC
* PCヘ音声を入力するもの，または仮想音源
* 任意のハードウェア
#### 仕様
アプリケーションは入力された音が，「衝撃」，「水」，「その他」のいずれのシーンの効果音に属するかを判断します。<br>
その後，シリアル信号を用いてマイコンボードにシリアルで判定結果を伝えます。<br>
プロトコルは以下の通り
* 衝撃:"i" (0x69)
* 水:"w" (0x77)
* その他:"e" (0x65)<br>
また，baudrateは115200bpsです。<br>
仕様にあうハードとマイコンプログラムを書いたら次へ！
### ソフト実行編
1. リリースページからzipファイルをダウンロードします。
2. まずzipファイルを解凍します。
3. コマンドプロンプトで解凍したディレクトリに移動します。
4. ``` ./main``` を実行します。
5. ```Please enter your input device index```というメッセージが出るので，ログに表示された入力機器情報から目的とする入力機器のindex番号を入力します。
6. ```No genuine Arduino found. Please choose and type your MCU port's index```と出た場合はログを参考にしてマイコンボードに接続されているポートのindex番号を入力します。`
7. ```Multiple port found. Please type your MCU port index```と出た場合はログを参考にして目的のマイコンが接続されているポートのindex番号を入力します。
8. 録音開始というログが出た場合，成功です！

# References
[1] Yahoo! Japan:Open Hack U 2020 Online(https://hacku.yahoo.co.jp/2020/)<br>
[2] Tensorflow:VGGish(https://github.com/tensorflow/models/tree/master/research/audioset/vggish)<br>
[3] Google Research:Audioset(https://research.google.com/audioset/)<br>
[4] IBM:audioset-classification(https://github.com/IBM/audioset-classification)<br>

# License
　ソースコードの権利については，特別な記載がない限りApache Lisence 2.0に準じます。<br>
　ソフトウェアの権利はリリースに同梱されているライセンスファイルに準じます。
