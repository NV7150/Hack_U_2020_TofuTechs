import unittest
import os
from PcEnv.vggish_parser import vggish_parser


class WavParseTestCase(unittest.TestCase):
    def test_parse(self):
        parser = vggish_parser()
        for i in range(10):
            parser.parse_with_vggish('./TestWavs/Tester.wav')


if __name__ == '__main__':
    unittest.main()
