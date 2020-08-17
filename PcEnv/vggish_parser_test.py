import unittest
import os
from PcEnv.vggish_parser import parse_with_vggish


class WavParseTestCase(unittest.TestCase):
    def test_parse(self):
        test_path = os.path.join('PcEnv', 'TestWavs', 'Tester.wav')
        val = parse_with_vggish('./TestWavs/Tester.wav')
        print(val)


if __name__ == '__main__':
    unittest.main()
