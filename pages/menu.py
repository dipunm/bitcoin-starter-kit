import badger2040
from consts.PageAliases import Aliases
from lib.input_manager import Input, InputManager
from lib.screen_updater import ScreenUpdater


class MenuPage:
    def __init__(self, inputs: InputManager, screen: ScreenUpdater) -> None:
        self.inputs = inputs
        self.screen = screen

    async def dice(self):
        print("going to dice!")
        self.inputs.stop()

    def drawUI(self):
        display = self.screen.display
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
        display = self.screen.display
        display.update_speed(badger2040.UPDATE_NORMAL)
        display.pen(15)
        display.clear()
        display.pen(0)

    async def start(self):
        # Setup inputs
        self.inputs.reset()
        self.inputs.register(Input.A, self.dice)
        
        # Draw initial view
        self.screen.display.led(95)
        self.clear()
        self.drawUI()
        
        # Refresh screen
        self.screen.start()
        self.screen.QueueUpdate(delay_ms=0)
        
        # Configure for fast refreshes
        
        # Start input listener
        await self.inputs.start()
        
        # Cleanup resources
        self.screen.stop()

        # Return to menu page when closed.
        return Aliases.dice_entropy