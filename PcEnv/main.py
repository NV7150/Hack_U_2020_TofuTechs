import os
import time
import glob

from PcEnv.RecordProcessor import RecordProcessor
from PcEnv.AudioRecorder import check_device


def process():
    size = check_device()

    i = 0
    while True:
        print('Please enter your input device index')
        i = int(input())
        if i < 0 or size <= i:
            print('invalid index')
        else:
            break

    print('selected ' + str(i))

    rec_pros = RecordProcessor(10, i, use_site=False)
    while True:
        i = input()
        if 'end' in i:
            rec_pros.is_end = True
            rec_pros.record_th.join()
            rec_pros.process_th.join()
            break


if __name__ == '__main__':
    # os.chdir('..')
    process()
