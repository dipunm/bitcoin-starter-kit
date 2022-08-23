from consts.PageAliases import Aliases
from lib.text_wall_mono import TextWallMono
import uasyncio
import badger2040
from lib.screen_updater import ScreenUpdater
from lib.input_manager import Input, InputManager

class DiceEntropyHexPage:
    def __init__(self, inputs: InputManager, screen: ScreenUpdater) -> None:
        self.inputs = inputs
        self.screen = screen
        self.textwall = TextWallMono(self.screen.display, 5, 5, 280, 108)
        self.textwall.setText(
"""123456 123456 123456 123456 123456 123456

123456 123456 123456 123456 123456 123456

123456 123456 123456 123456 123456 123456

123456 123456 123456 123456 123456 1234--"""
        )

        self.textwall2 = TextWallMono(self.screen.display, 2, 3, 280, 112)
        self.textwall2.setText(
"""
 A B 0  F F 3  E E F  8 8 3  2 8 3  4 8 F

 A 0 0  0 B C  A B 0  F F 3  E E F  8 8 3

 2 8 3  4 8 F  A 0 0  0 B C  A B 0  F F 3

 E E F  8 8 3  A B 0  F F 3  E E F  8 8 -"""
        )

    def prepareUI(self):
        display = self.screen.display
        
        # Clear the UI areas
        display.pen(15)
        display.rectangle(0, 114, 296, 15)
        display.rectangle(287, 0, 10, 128)
        
        display.pen(0)
        display.line(0, 114, 287, 114)
        display.line(287, 0, 287, 115)

        display.pen(0)
        display.thickness(1)
        display.font("bitmap8")
        display.text("OK", 32, 118, 1)
        
        if self.textwall.canScrollUp():
            display.text("U", 291, 23, 1.5)
            display.text("P", 291, 32, 1.5)
        
        if self.textwall.canScrollDown():
            display.text("D", 291, 75, 1.5)
            display.text("O", 291, 84, 1.5)
            display.text("W", 291, 93, 1.5)
            display.text("N", 291, 102, 1.5)
        
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
        if not self.textwall.canScrollDown():
            return
        
        self.textwall.scrollDown()
        self.textwall.render()
        self.prepareUI()
        self.screen.QueueUpdate(delay_ms=300)

    async def scrollUp(self):
        if not self.textwall.canScrollUp():
            return
        
        self.textwall.scrollUp()
        self.textwall.render()
        self.prepareUI()
        self.screen.QueueUpdate(delay_ms=300)

    async def start(self):
        # Setup inputs
        self.inputs.reset()
        self.inputs.register(Input.A, self.nextPage)    
        self.inputs.register(Input.UP, self.scrollUp)
        self.inputs.register(Input.DOWN, self.scrollDown)
        
        # Draw initial view
        self.screen.display.led(95)
        self.clear()
        self.prepareUI()
        self.textwall.render()
        self.textwall2.render(clearSpace=False)

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
