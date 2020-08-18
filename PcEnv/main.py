from PcEnv.RecordProcessor import RecordProcessor
import time

if __name__ == '__main__':
    rec_pros = RecordProcessor(10)
    time.sleep(100)
    rec_pros.is_end = True
    rec_pros.record_th.join()
    rec_pros.process_th.join()
