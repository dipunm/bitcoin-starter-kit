from time import sleep
import badger2040
from badger2040 import UPDATE_NORMAL, UPDATE_FAST
from lib.drawDice import drawDice, drawIndicator
import uasyncio
from lib.debounce import monitorPinOnce, monitorPin, firstPinActivate
from lib.diceCount import ThreadSafeCounter
import ui
from lib.screen_updater import ScreenUpdater

badger2040.system_speed(badger2040.SYSTEM_FAST)

display = badger2040.Badger2040()

display.led(95)
display.update_speed(UPDATE_NORMAL)
display.pen(15)
display.clear()
display.update()
display.update_speed(UPDATE_FAST)


button_a = machine.Pin(badger2040.BUTTON_A, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_b = machine.Pin(badger2040.BUTTON_B, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_c = machine.Pin(badger2040.BUTTON_C, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_up = machine.Pin(badger2040.BUTTON_UP, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_down = machine.Pin(badger2040.BUTTON_DOWN, machine.Pin.IN, machine.Pin.PULL_DOWN)

ui.draw(display)
drawIndicator(display, 0, update=False)
display.update()


display.led(0)

updater = ScreenUpdater(display)

inputDiceLock = uasyncio.Lock()
async def inputDice(diceCounter, posCounter):
    global updater, autoPin
    async def noop(pin):
        return

    updater.DelayAnyUpdate()
    if inputDiceLock.locked():
        await diceCounter.inc()
    else:
        await diceCounter.reset()
        pos = await posCounter.get()
        async with inputDiceLock:
            try:
                for i in range(6):
                    pin = await uasyncio.wait_for_ms(firstPinActivate(button_a, button_b, button_c), 500)
                    if pin == button_a:
                        await inputDice(diceCounter, posCounter)
                    else:
                        autoPin=pin
                        raise uasyncio.TimeoutError()
                while True:
                    pin = await uasyncio.wait_for_ms(firstPinActivate(button_a, button_b, button_c), 500)
                    if pin == button_a:
                        continue
                    else:
                        autoPin=pin
                        raise uasyncio.TimeoutError()
            except uasyncio.TimeoutError:
                count = await diceCounter.get()
                drawDice(display, pos, count%6+1, update=False)
                updater.QueueUpdate()
                return autoPin


async def back(counter):
    global updater
    updater.DelayAnyUpdate()
    await counter.dec()
    drawIndicator(display, await counter.get(), update=False)
    updater.QueueUpdate()

async def ok(counter):
    global updater
    updater.DelayAnyUpdate()
    await counter.inc()
    drawIndicator(display, await counter.get(), update=False)
    updater.QueueUpdate()

autoPin=None
async def main():
    global autoPin
    diceCounter = ThreadSafeCounter(6)
    posCounter = ThreadSafeCounter(132)
    while True:
        pin = await firstPinActivate(button_a, button_b, button_c, button_up) if autoPin == None else autoPin
        autoPin = None
        if pin == button_a:
            autoPin = await inputDice(diceCounter, posCounter)
        elif pin == button_b:
            await back(posCounter)
        elif pin == button_c:
            await ok(posCounter)

updater.start()
uasyncio.run(main())
