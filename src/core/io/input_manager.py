import uasyncio
import badger2040
import machine
from core.util.asynclib import oneOf

async def wait_pin_value(pin, value):
    active = 0
    while active < 20:
        if pin.value() == value:
            active += 1
        else:
            active = 0
        await uasyncio.sleep_ms(1)

async def wait_pin_activate(pin):
    if pin.value() != 0:
        await wait_pin_value(pin, 0)
    await wait_pin_value(pin, 1)
    return pin


class Input:
    def __init__(self, name: str, pin):
        self.val = pin
        self.name = name
        self.id = id(pin)

Input.A = Input(badger2040.BUTTON_A, machine.Pin(badger2040.BUTTON_A, machine.Pin.IN, machine.Pin.PULL_DOWN))
Input.B = Input(badger2040.BUTTON_B, machine.Pin(badger2040.BUTTON_B, machine.Pin.IN, machine.Pin.PULL_DOWN))
Input.C = Input(badger2040.BUTTON_C, machine.Pin(badger2040.BUTTON_C, machine.Pin.IN, machine.Pin.PULL_DOWN))
Input.UP = Input(badger2040.BUTTON_UP, machine.Pin(badger2040.BUTTON_UP, machine.Pin.IN, machine.Pin.PULL_DOWN))
Input.DOWN = Input(badger2040.BUTTON_DOWN, machine.Pin(badger2040.BUTTON_DOWN, machine.Pin.IN, machine.Pin.PULL_DOWN))

class InputManager:
    actionMap: dict

    def __init__(self) -> None:
        self.actionMap = {}
        self.pinMap = {}
        self.endEvent = uasyncio.Event()

    def register(self, input: Input, action):
        self.actionMap[input.id] = action
        self.pinMap[input.id] = input.val

    def reset(self):
        self.actionMap = {}
        self.pinMap = {}

    def stop(self):
        self.ended = True
        self.endEvent.set()

    async def firstPinActivate(self) -> Input:
        return await oneOf(
            *map(wait_pin_activate, self.pinMap.values())
        )

    async def start(self):
        self.ended = False
        while not self.ended:
            pin = await oneOf(
                    self.firstPinActivate(),
                    self.endEvent.wait(),
            )

            if self.endEvent.is_set():
                self.endEvent.clear()
                break

            uasyncio.create_task(self.actionMap[id(pin)]())