import time
import _thread

class ScreenUpdater:
    def __init__(self, display):
        self.thread_exit = False
        self.display = display
        self.variableLock = _thread.allocate_lock()
        self.runningLock = _thread.allocate_lock()
        self.needs_update = False
        self.update_time = time.ticks_ms()

    def start(self):
        self.thread = _thread.start_new_thread(self._main, ())
        
    def stop(self):
        self.thread_exit = True
        while True:
            if self.runningLock.locked():
                time.sleep(0.1)
            else:
                break

    def QueueUpdate(self, delay_ms = 500):
        self.variableLock.acquire()
        self.needs_update = True
        self.variableLock.release()
        self.DelayAnyUpdate(delay_ms=delay_ms)

    def DelayAnyUpdate(self, delay_ms = 500):
        self.variableLock.acquire()
        self.update_time = time.ticks_add(time.ticks_ms(), delay_ms)
        self.variableLock.release()

    def _main(self):
        time.sleep(1)
        self.runningLock.acquire()
        self.thread_exit = False
        while not self.thread_exit:
            self.variableLock.acquire()
            diff = time.ticks_diff(self.update_time, time.ticks_ms())
            if self.needs_update and diff <= 0:
                self.needs_update = False
                self.variableLock.release()
                self.display.update()
            else:
                self.variableLock.release()
            time.sleep(0.01)

        self.runningLock.release()
        _thread.exit()

