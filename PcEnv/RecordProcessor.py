from PcEnv.SerialCommunicator import SerialCommunicator
from PcEnv.SoundJudger import SoundJudge

path_wav = './RecordWav.wav'
index = 2
baud_rate = 115200


class RecordProcessor:
    def __init__(self, sample_sec):
        self.judge = SoundJudge(sample_sec, path_wav, index)
        self.s_com = SerialCommunicator(baud_rate)

    def process(self):

        code = self.judge.record_and_judge()

        pass

        print(code)

        if code == 'water':
            command = 'w'
        elif code == 'impact':
            command = 'i'
        elif code == 'else':
            command = 'e'
        else:
            command = 'N/A'

        if command != 'N/A':
            self.s_com.send_serial(command)

    def close(self):
        self.s_com.close_serial()