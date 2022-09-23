import uasyncio
import badger2040

import apps.menu as menu
import apps.mnemonic_creator.screens.dice_entropy as dice_entropy
from core.io.input_manager import Input
from core.presentation.text_wall_mono import TextWallMono

from core.io import inputManager, screenUpdater, display

class DiceEntropyHexPage:
    def __init__(self) -> None:
        self.textwall = TextWallMono(display, 5, 5, 280, 108)
        self.textwall.setText(
"""123456 123456 123456 123456 123456 123456

123456 123456 123456 123456 123456 123456

123456 123456 123456 123456 123456 123456

123456 123456 123456 123456 123456 1234--"""
        )

        self.textwall2 = TextWallMono(display, 2, 3, 280, 112)
        self.textwall2.setText(
"""
 A B 0  F F 3  E E F  8 8 3  2 8 3  4 8 F

 A 0 0  0 B C  A B 0  F F 3  E E F  8 8 3

 2 8 3  4 8 F  A 0 0  0 B C  A B 0  F F 3

 E E F  8 8 3  A B 0  F F 3  E E F  8 8 -"""
        )

    def prepareUI(self):        
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
        display.update_speed(badger2040.UPDATE_NORMAL)
        display.pen(15)
        display.clear()
        display.pen(0)
        
    async def nextPage(self):
        self.goto = dice_entropy.DiceEntropyPage().start
        inputManager.stop()

    async def scrollDown(self):
        if not self.textwall.canScrollDown():
            return
        
        self.textwall.scrollDown()
        self.textwall.render()
        self.prepareUI()
        screenUpdater.QueueUpdate(delay_ms=300)

    async def scrollUp(self):
        if not self.textwall.canScrollUp():
            return
        
        self.textwall.scrollUp()
        self.textwall.render()
        self.prepareUI()
        screenUpdater.QueueUpdate(delay_ms=300)

    async def start(self):
        # Setup inputs
        inputManager.reset()
        inputManager.register(Input.A, self.nextPage)    
        inputManager.register(Input.UP, self.scrollUp)
        inputManager.register(Input.DOWN, self.scrollDown)
        
        # Draw initial view
        display.led(95)
        self.clear()
        self.prepareUI()
        self.textwall.render()
        self.textwall2.render(clearSpace=False)

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
        return self.goto or menu.start()
