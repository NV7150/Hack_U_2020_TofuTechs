import unittest
from PcEnv.RecordProcessor import RecordProcessor

class MyTestCase(unittest.TestCase):
    def test_something(self):
        rec = RecordProcessor(10)
        rec.process()


if __name__ == '__main__':
    unittest.main()
