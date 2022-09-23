import badger2040
from core.io.input_manager import Input
from core.io import display, inputManager, screenUpdater
import apps.mnemonic_creator as mnemonic_creator

class MenuPage:
    def __init__(self) -> None:
        pass

    async def dice(self):
        print("going to dice!")
        inputManager.stop()

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


    def clear(self):
        display.update_speed(badger2040.UPDATE_NORMAL)
        display.pen(15)
        display.clear()
        display.update()
        display.pen(0)
        display.clear()
        display.update()
        display.pen(15)
        display.clear()
        display.update()
        display.pen(0)

    async def start(self):
        # Setup inputs
        inputManager.reset()
        inputManager.register(Input.A, self.dice)
        
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
        
        # Cleanup resources
        screenUpdater.stop()

        # Return to menu page when closed.
        return mnemonic_creator.run