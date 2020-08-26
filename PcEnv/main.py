import os
import time

# Attention! 実行の前にRecordProcessor.pyのindexを確認!

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

    rec_pros = RecordProcessor(10, i, use_site=True)
    while True:
        i = input()
        if 'end' in i:
            rec_pros.is_end = True
            rec_pros.record_th.join()
            rec_pros.process_th.join()
            break


def device_check():
    check_device()


if __name__ == '__main__':
    process()
    # check_device()
