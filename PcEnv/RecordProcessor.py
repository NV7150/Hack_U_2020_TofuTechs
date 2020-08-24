import threading
import os

from PcEnv.SerialCommunicator import SerialCommunicator
from PcEnv.SoundJudger import SoundJudge
from PcEnv.AudioRecorder import AudioRecorder
from PcEnv.FileLocker import FileLocker
from PcEnv.RemoteController import remoteAction

path_wav = os.path.join(os.path.dirname(__file__), 'RecordWav.wav')
path_wav_process = os.path.join(os.path.dirname(__file__), 'ProcessWav.wav')
# インデックス
# ハードの環境だと1に設定すること！
index = 2
baud_rate = 115200


def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func


class RecordProcessor:
    def __init__(self, sample_sec):
        self.audioRec = AudioRecorder(index, path_wav)
        self.sample_sec = sample_sec
        self.judge = SoundJudge(sample_sec, path_wav_process, index)
        self.s_com = SerialCommunicator(baud_rate)
        self.record_th = threading.Thread(target=self.record)
        self.process_th = threading.Thread(target=self.process)
        self.is_end = False
        self.is_new_record_setted = False
        self.fileLocker = FileLocker()

        self.record_th.start()
        self.process_th.start()

    @synchronized
    def flag_new_record(self, set_flag=False, setting=True):
        if setting:
            self.is_new_record_setted = set_flag
        return self.is_new_record_setted

    def record(self):
        while not self.is_end:
            self.audioRec.record(self.sample_sec, locker=self.fileLocker)
            self.flag_new_record(set_flag=True)

    def process(self):
        while not self.is_end:
            if not self.flag_new_record(setting=False):
                continue

            self.flag_new_record(set_flag=False)

            while self.fileLocker.is_lock:
                pass
            self.fileLocker.lock()
            os.remove(path_wav_process)
            os.rename(path_wav, path_wav_process)
            self.fileLocker.unlock()

            code = self.judge.record_and_judge()

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

            if code == 'impact':
                remoteAction()

        self.s_com.close_serial()
