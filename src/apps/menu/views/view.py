from core.io import display, inputManager, screenUpdater
from core.io.input_manager import Input
from core.base.iview import IView
import badger2040

class MenuView(IView):
    def clear(self):
        display.update_speed(badger2040.UPDATE_NORMAL)
        display.pen(0)
        display.clear()
        display.update()
        display.pen(15)
        display.clear()
        display.update()

    def drawUI(self):
        display.pen(0)
        display.thickness(1)
        display.rectangle(10, 20, 70, 70)

        display.pen(0)
        display.thickness(1)
        display.font("bitmap8")
        display.text("dice", 32, 118, 1)
        display.text("words", 139, 118, 1)
        display.text("xor", 247, 118, 1)

    async def start(self, controller):
        # Setup inputs
        inputManager.register(Input.A, controller.gotoMnemonicCreator)

        # Draw initial view
        display.led(95)
        self.clear()
        self.drawUI()

        # Update screen
        screenUpdater.start()
        screenUpdater.QueueUpdate()        

        # Configure for fast refreshes
        display.update_speed(badger2040.UPDATE_FAST)

        # Start input listener
        await inputManager.start()


    async def dispose(self):
        inputManager.stop()
        screenUpdater.stop()
        inputManager.reset()
