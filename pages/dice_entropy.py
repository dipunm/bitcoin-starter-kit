import uasyncio
import badger2040
from utils.asynclib import oneOf
from views.dice_array import drawDice, drawIndicator
from lib.counter import Counter
from lib.screen_updater import ScreenUpdater
from lib.input_manager import Input, InputManager

async def sleep_ms(ms):
    # uasyncio.sleep_ms cannot be passed 
    # directly into uasyncio.create_task :/
    return await uasyncio.sleep_ms(ms)

class DiceEntropyPage:
    def __init__(self, inputs: InputManager, screen: ScreenUpdater) -> None:
        self.inputs = inputs
        self.screen = screen
        self.pos = Counter(0, 131) # 0 - 131 inclusive, total: 132
        self.comboPressLock = uasyncio.Lock()
        self.comboBreakEvent = uasyncio.Event()
        self.comboAddEvent = uasyncio.Event()

    async def count(self):
        if self.comboPressLock.locked():
            self.comboAddEvent.set()
        else:
            dice = Counter(1, 6) # 1 - 6 inclusive
            pos = self.pos.get()
            async with self.comboPressLock:
                while True:
                    self.comboBreakEvent.clear()
                    self.comboAddEvent.clear()
                    await oneOf(
                        sleep_ms(500),
                        self.comboAddEvent.wait(),
                        self.comboBreakEvent.wait()
                    )

                    if self.comboAddEvent.is_set():
                        dice.increment()
                        self.comboAddEvent.clear()
                        continue
                    else:
                        break
    
            drawDice(self.screen.display, pos, dice.get())
            await self.next()

            
    async def next(self):
        self.comboBreakEvent.set()
        self.screen.DelayAnyUpdate()
        self.pos.increment()
        drawIndicator(self.screen.display, self.pos.get())
        self.screen.QueueUpdate(delay_ms=10)


    async def back(self):
        self.comboBreakEvent.set()
        self.screen.DelayAnyUpdate()
        self.pos.decrement()
        drawIndicator(self.screen.display, self.pos.get())
        self.screen.QueueUpdate(delay_ms=10)

    def prepareUI(self):
        display = self.screen.display
        display.pen(0)
        display.line(0, 114, 287, 114)
        display.line(287, 0, 287, 115)

        display.pen(0)
        display.thickness(1)
        display.font("bitmap8")
        display.text("count", 32, 118, 1)
        display.text("back", 139, 118, 1)
        display.text("next", 247, 118, 1)

        display.thickness(2)
        display.text("C", 290, 29, 1.5)
        display.text("Q", 290, 90, 1.5)
        display.thickness(1)

    def clear(self):
        display = self.screen.display
        display.update_speed(badger2040.UPDATE_NORMAL)
        display.pen(15)
        display.clear()
        display.pen(0)

    async def start(self):
        # Setup inputs
        self.inputs.reset()
        self.inputs.register(Input.A, self.count)
        self.inputs.register(Input.B, self.back)
        self.inputs.register(Input.C, self.next)
        
        # Draw initial view
        self.screen.display.led(95)
        self.clear()
        self.prepareUI()
        drawIndicator(self.screen.display, 0)

        # Refresh screen
        self.screen.start()
        self.screen.QueueUpdate(delay_ms=0)
        await uasyncio.sleep_ms(50)
        
        # Configure for fast refreshes
        self.screen.display.update_speed(
            badger2040.UPDATE_FAST
        )
        self.screen.display.led(0)

        # Start input listener
        await self.inputs.start()
