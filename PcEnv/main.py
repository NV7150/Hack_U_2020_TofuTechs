import os
import time

os.chdir('../..')


from PcEnv.RecordProcessor import RecordProcessor
from PcEnv.AudioRecorder import check_device


def process():
    rec_pros = RecordProcessor(10)
    while True:
        i = input()
        if 'end' in i:
            rec_pros.is_end = True
            rec_pros.record_th.join()
            rec_pros.process_th.join()


def device_check():
    check_device()


if __name__ == '__main__':
    process()
    # check_device()

