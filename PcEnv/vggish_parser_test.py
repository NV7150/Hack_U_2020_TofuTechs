import unittest
import os
import sys
from PcEnv.vggish_parser import vggish_parser
from PcEnv.run import get_model, get_label
from PcEnv.audioTest import record
import tensorflow as tf


class WavParseTestCase(unittest.TestCase):

    def test_all(self):
        parser = vggish_parser()
        record('./Test/test.wav')
        data_v = parser.parse_with_vggish('./Test/test.wav')
        sliced_data_v = []

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
        print(d_ts)

        model = get_model()

        a = model.predict(d_ts)

        print(a)


if __name__ == '__main__':
    sys.path.append('PcEnv/models/research/audioset/vggish')
    unittest.main()
