import unittest
import os
import sys
from PcEnv.SoundJudger import SoundJudge
from PcEnv.SerialCommunicator import SerialCommunicator
import tensorflow as tf


# class WavParseTestCase(unittest.TestCase):
#
#     def test_all(self):
#         judge = SoundJudge(10, './TestWavs/Test', 3)
#         print(judge.record_and_judge())


class SerialTestCase(unittest.TestCase):
    def test_serial(self):
        comm = SerialCommunicator(9600)
        comm.send_serial('a')


if __name__ == '__main__':
    unittest.main()
