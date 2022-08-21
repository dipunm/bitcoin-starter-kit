from consts.PageAliases import Aliases
from lib.text_wall import TextWall
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

class DiceEntropyInfoPage:
    def __init__(self, inputs: InputManager, screen: ScreenUpdater) -> None:
        self.inputs = inputs
        self.screen = screen
        self.textwall = TextWall(self.screen.display, 5, 5, 280, 108)
        self.textwall.setText("""Dice entropy
        
        Dice rolls is a great source of entropy. 132 rolls will allow us to generate 256bits of entropy in a verifiable way. Visit https://www.dipunmistry.co.uk/... for more details.

        After each die roll, press the button labelled 'count' multiple times to record each result.

        You can use the prev and next buttons to make ammendments if necessary.

        To continue, press OK
        """)

    def prepareUI(self):
        display = self.screen.display
        display.pen(0)
        display.line(0, 114, 287, 114)
        display.line(287, 0, 287, 115)

        display.pen(0)
        display.thickness(1)
        display.font("bitmap8")
        display.text("OK", 32, 118, 1)
        
        display.thickness(1)
        display.text("U", 291, 23, 1.5)
        display.text("P", 291, 32, 1.5)
        
        display.text("D", 291, 75, 1.5)
        display.text("O", 291, 84, 1.5)
        display.text("W", 291, 93, 1.5)
        display.text("N", 291, 102, 1.5)
        display.thickness(1)

    def clear(self):
        display = self.screen.display
        display.update_speed(badger2040.UPDATE_NORMAL)
        display.pen(15)
        display.clear()
        display.pen(0)
        
    async def nextPage(self):
        self.goto = Aliases.dice_entropy
        self.inputs.stop()

    async def scrollDown(self):
        self.textwall.scrollDown()
        self.textwall.render()
        self.screen.QueueUpdate(delay_ms=10)

    async def start(self):
        # Setup inputs
        self.inputs.reset()
        self.inputs.register(Input.A, self.nextPage)
        self.inputs.register(Input.DOWN, self.scrollDown)
        
        # Draw initial view
        self.screen.display.led(95)
        self.clear()
        self.prepareUI()
        self.textwall.render()

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
        
        # Cleanup resources
        self.screen.stop()

        # Return to menu page when closed.
        return self.goto or Aliases.menu
