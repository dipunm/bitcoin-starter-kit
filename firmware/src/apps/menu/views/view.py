from core.io import display, inputManager, screenUpdater
from core.io.input_manager import Input
from core.base.iview import IView
from core.util.image import readImagePy
import badger2040

import bin.Checksum
import bin.Keys
import bin.Compose

class MenuView(IView):
    def clear(self):
        display.update_speed(badger2040.UPDATE_NORMAL)
        display.pen(15)
        display.clear()
        display.update()

    def drawUI(self):
        display.pen(0)
        display.thickness(1)
        display.image(readImagePy(bin.Checksum), 96, 96, 0, 0)
        display.image(readImagePy(bin.Keys), 96, 96, 98, 0)
        display.image(readImagePy(bin.Compose), 96, 96, 196, 0)

        display.pen(0)
        display.thickness(1)
        display.font("sans")
        display.text("GENERATE", 16, 108, 0.45)
        display.text("MANAGE", 123, 108, 0.45)
        display.text("COMBINE", 211, 108, 0.45)

    async def start(self, controller):
        # Setup inputs
        inputManager.register(Input.A, controller.gotoChecksum)

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
