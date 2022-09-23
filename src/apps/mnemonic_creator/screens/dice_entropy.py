import uasyncio
import badger2040
import apps.menu as menu
from core.util.asynclib import oneOf
from apps.mnemonic_creator.helpers.die_renderer import drawDice, drawIndicator
from core.tracking.counter import Counter
from core.io.input_manager import Input
from core.io import display, inputManager, screenUpdater

async def sleep_ms(ms):
    # uasyncio.sleep_ms cannot be passed 
    # directly into uasyncio.create_task :/
    return await uasyncio.sleep_ms(ms)

class DiceEntropyPage:
    def __init__(self) -> None:
        self.pos = Counter(0, 141) # 0 - 131 inclusive, total: 132
        self.comboPressLock = uasyncio.Lock()
        self.comboBreakEvent = uasyncio.Event()
        self.comboAddEvent = uasyncio.Event()
        self.diceCapture = [0] * 142 # array of 0's 132 times

    async def count(self):
        if self.comboPressLock.locked():
            self.comboAddEvent.set()
        else:
            pos = self.pos.get()
            dice = Counter(1, 6, loop=True) # 1 - 6 inclusive

            print("START>>", self.diceCapture[pos])
            if (self.diceCapture[pos] != 0):
                dice.set(self.diceCapture[pos] + 1)

            self.diceCapture[pos] = dice.get()
            print("DICE>>>:", dice.get(), pos, self.diceCapture[pos])
            change = True
            async with self.comboPressLock:
                while True:
                    self.comboBreakEvent.clear()
                    self.comboAddEvent.clear()
                    if change == True:
                        await oneOf(
                            sleep_ms(500),
                            self.comboAddEvent.wait(),
                            self.comboBreakEvent.wait()
                        )
                    else:
                        await oneOf(
                            self.comboAddEvent.wait(),
                            self.comboBreakEvent.wait()
                        )


                    was_timeout = not self.comboAddEvent.is_set() and not self.comboBreakEvent.is_set()

                    if was_timeout:
                        change = False
                        self.redrawAll()
                        screenUpdater.QueueUpdate(delay_ms=10)
                        break
                    elif self.comboAddEvent.is_set():
                        dice.increment()
                        self.diceCapture[pos] = dice.get()
                        change = True
                        self.comboAddEvent.clear()
                        continue
                    else:
                        break
            
            if change:
                change = False
                self.redrawAll()
                screenUpdater.QueueUpdate(delay_ms=10)

            
    async def next(self):
        self.comboBreakEvent.set()
        if self.diceCapture[self.pos.get()] == 0:
            # Current dice not set, do not progress.
            return

        if self.pos.get() == len(self.diceCapture) - 1:
            return
        
        self.pos.increment()
        if not self.comboPressLock.locked():
            self.redrawAll()
            screenUpdater.QueueUpdate(delay_ms=10)


    async def back(self):
        self.comboBreakEvent.set()
        if self.pos.get() < 1:
            # No need to decrement or refresh the screen
            return

        self.pos.decrement()
        if not self.comboPressLock.locked():
            self.redrawAll()
            screenUpdater.QueueUpdate(delay_ms=10)

    async def exit(self):
        print("going to menu")
        inputManager.stop()
        
    def redrawAll(self):
        display.pen(15)
        display.clear()
        display.pen(0)

        if self.pos.get() > 132:
            for i in range(0, 142): # exclusive (132 is omitted)
                if self.diceCapture[i] == 0:
                    break

                drawDice(display, i, self.diceCapture[i], shiftY=11)
            drawIndicator(display, self.pos.get(), shiftY=11)
        else:
            for i in range(0, 142): # exclusive (132 is omitted)
                if self.diceCapture[i] == 0:
                    break

                drawDice(display, i, self.diceCapture[i])
            drawIndicator(display, self.pos.get())

        self.prepareUI()


    def prepareUI(self):
        display.pen(15)
        display.rectangle(0, 114, 296, 15)
        display.rectangle(287, 0, 10, 128)

        display.pen(0)
        display.line(0, 114, 287, 114)
        display.line(287, 0, 287, 115)

        display.pen(0)
        display.thickness(1)
        display.font("bitmap8")
        display.text("count", 32, 118, 1)
        display.text("prev", 139, 118, 1)
        display.text("next", 247, 118, 1)

        display.text("Q", 291, 14, 1.5)
        display.text("U", 291, 23, 1.5)
        display.text("I", 291, 32, 1.5)
        display.text("T", 291, 41, 1.5)
        
        if self.canComplete():
            display.text("D", 291, 75, 1.5)
            display.text("O", 291, 84, 1.5)
            display.text("N", 291, 93, 1.5)
            display.text("E", 291, 102, 1.5)
        
    def clear(self):
        display.update_speed(badger2040.UPDATE_NORMAL)
        display.pen(15)
        display.clear()
        display.pen(0)

    def canComplete(self):
        return len(list(filter(lambda x: x == 0, self.diceCapture))) == 0

    async def done(self):
        if not self.canComplete():
            return
        
        print("I WOULD WORK!!!")
    
    async def start(self):
        # Setup inputs
        inputManager.reset()
        inputManager.register(Input.A, self.count)
        inputManager.register(Input.B, self.back)
        inputManager.register(Input.C, self.next)
        inputManager.register(Input.UP, self.exit)
        inputManager.register(Input.DOWN, self.done)
        
        # Draw initial view
        display.led(95)
        self.clear()
        self.prepareUI()
        drawIndicator(display, 0)

        # Refresh screen
        screenUpdater.start()
        screenUpdater.QueueUpdate(delay_ms=0)
        await uasyncio.sleep_ms(50)
        
        # Configure for fast refreshes
        display.update_speed(
            badger2040.UPDATE_FAST
        )
        display.led(0)

        # Start input listener
        await inputManager.start()
        
        # Cleanup resources
        screenUpdater.stop()

        # Return to menu page when closed.
        return menu.run
