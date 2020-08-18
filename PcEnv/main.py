from PcEnv.RecordProcessor import RecordProcessor

if __name__ == '__main__':
    rec_pros = RecordProcessor(10)
    for i in range(10):
        rec_pros.process()
    rec_pros.close()
