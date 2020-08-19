import threading


def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func


class FileLocker:
    def __init__(self):
        self.is_lock = False

    @synchronized
    def lock(self):
        self.is_lock = True

    @synchronized
    def unlock(self):
        self.is_lock = False
