import unittest
import os
import sys
from PcEnv.SoundJudger import SoundJudge
import tensorflow as tf


class WavParseTestCase(unittest.TestCase):

    def test_all(self):
        judge = SoundJudge(10, './TestWavs/Test', 3)
        print(judge.record_and_judge())


if __name__ == '__main__':
    unittest.main()
