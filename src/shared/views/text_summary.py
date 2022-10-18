import badger2040
import uasyncio
from core.io import display, inputManager, screenUpdater
from core.base.iview import IView
from core.io.input_manager import Input
from core.presentation.text_wall import TextWall

class TextSummaryView(IView):
    def __init__(self, msg, action) -> None:
        self.textwall = TextWall(display, 5, 5, 280, 108)
        self.textwall.setText(msg)
        self.action = action

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

    async def start(self, controller):
        # Setup inputs
        inputManager.register(Input.A, self.action)
        inputManager.register(Input.UP, self.scrollUp)
        inputManager.register(Input.DOWN, self.scrollDown)

        # Draw initial view
        display.led(95)
        self.clear()
        self.prepareUI()
        self.textwall.render()

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
        
    async def dispose(self):
        inputManager.stop()
        inputManager.reset()
        screenUpdater.stop()
