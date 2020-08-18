import tensorflow as tf
import numpy as np

from PcEnv.VggishParser import VggishParser
from PcEnv.AudioRecorder import AudioRecorder
from PcEnv.run import get_model, get_label


class SoundJudge:
    def __init__(self, sample_time: float, wav_path: str, device_index: int):
        self.sample_time = sample_time
        self.parser = VggishParser()
        self.wav_path = wav_path
        self.label = get_label()
        self.model = get_model()

    def record_and_judge(self):
        data_v = self.parser.parse_with_vggish(self.wav_path)

        if len(data_v) > 10:
            sliced_data_v = data_v[:10]
        elif len(data_v) < 10:
            sliced_data_v = data_v
            for i in range(10 - len(data_v)):
                row = []
                for j in range(128):
                    row.append(0)
                sliced_data_v.append(row)
        else:
            sliced_data_v = data_v

        d_ts = tf.multiply(sliced_data_v, 1)
        d_ts = tf.expand_dims(d_ts, 0)

        predict_value = self.model.predict(d_ts)
        print(predict_value)
        return self.label[np.argmax(predict_value[0])]
