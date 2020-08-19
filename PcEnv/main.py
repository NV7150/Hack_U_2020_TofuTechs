import time
import os

from PcEnv.RecordProcessor import RecordProcessor
from PcEnv.AudioRecorder import check_device


os.chdir('../..')

def process():
    rec_pros = RecordProcessor(10)
    time.sleep(100)
    rec_pros.is_end = True
    rec_pros.record_th.join()
    rec_pros.process_th.join()

def device_check():
    check_device()


if __name__ == '__main__':
    # process()
    check_device()