import time
import _thread
import uasyncio
from badger2040 import Badger2040

class UpdateBox:
    x: int 
    y: int 
    w: int 
    h: int

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class ScreenUpdater:
    def __init__(self, display: Badger2040):
        self.thread_exit = False
        self.display = display
        self.variableLock = _thread.allocate_lock()
        self.runningLock = _thread.allocate_lock()
        self.needs_update = False
        self.update_time = time.ticks_ms()
        self.partialQueue: list[UpdateBox] = []

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

    def QueuePartialUpdate(self, box: UpdateBox, delay_ms = 0):
        uasyncio.create_task(self._updatePartial(box, delay_ms))

    def DelayAnyUpdate(self, delay_ms = 500):
        self.variableLock.acquire()
        self.update_time = time.ticks_add(time.ticks_ms(), delay_ms)
        self.variableLock.release()


    async def _updatePartial(self, box: UpdateBox, delay_ms = 0):
        await uasyncio.sleep_ms(delay_ms)
        self.variableLock.acquire()
        self.partialQueue.append(box)
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
                self.partialQueue.clear()
                self.variableLock.release()

                self.display.update()

            elif len(self.partialQueue) > 0:
                tmpQueue = self.partialQueue.copy()
                self.partialQueue.clear()
                self.variableLock.release()

                for i in range(0, len(tmpQueue)):
                    self.display.partial_update(
                        tmpQueue[i].x,
                        # y position must be multiple of 8
                        tmpQueue[i].y - tmpQueue[i].y%8,
                        tmpQueue[i].w,
                        # height must be multiple of 8
                        tmpQueue[i].h - tmpQueue[i].h%8 + 8 
                    )
            else: 
                self.variableLock.release()
            time.sleep(0.01)

        self.runningLock.release()
        _thread.exit()

