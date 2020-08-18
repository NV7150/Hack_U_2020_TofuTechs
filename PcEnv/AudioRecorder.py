'''
    音声入力テスト用
'''

# -*- coding: utf-8 -*
import pyaudio
import wave


class AudioRecorder:
    def __init__(self, device_index: int, file_path: str):
        self.device_index = device_index
        self.file_path = file_path

    def record(self, rec_time):
        fmt = pyaudio.paInt16  # 音声のフォーマット
        ch = 1  # チャンネル1(モノラル)
        sampling_rate = 44100  # サンプリング周波数(入力機器に合わせて)
        chunk = 2 ** 11  # チャンク（データ点数）
        audio = pyaudio.PyAudio()
        index = self.device_index  # 録音デバイスのインデックス番号

        # インデックスは https://algorithm.joho.info/programming/python/pyaudio-device-index/ こことか見て
        stream = audio.open(format=fmt, channels=ch, rate=sampling_rate, input=True,
                            input_device_index=index,
                            frames_per_buffer=chunk)
        print("録音開始")

        # 録音処理
        frames = []

        for i in range(int(sampling_rate / chunk * rec_time)):
            data = stream.read(chunk)
            frames.append(data)

        print("recording  end...")

        # 録音終了処理
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # 録音データをファイルに保存
        wav = wave.open(self.file_path, 'wb')
        wav.setnchannels(ch)
        wav.setsampwidth(audio.get_sample_size(fmt))
        wav.setframerate(sampling_rate)
        wav.writeframes(b''.join(frames))
        wav.close()


def check_device():
    audio = pyaudio.PyAudio()

    # 音声デバイス毎のインデックス番号を一覧表示
    for x in range(0, audio.get_device_count()):
        print(audio.get_device_info_by_index(x))
