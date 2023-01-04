from core.consts import SCREEN_WIDTH
from core.io import display, inputManager, screenUpdater
from core.io.input_manager import Input
from core.base.iview import IView
import badger2040

from core.presentation.controls_bar import ControlsBar
from core.presentation.text_wall import TextWall
from core.presentation.text_wall_mono import TextWallMono


class DataInputView(IView):
    def __init__(self) -> None:
        self.controlsUI = ControlsBar(display, A="<-", B="Select", C="->", UP="D", DOWN="Z")
        self.keyboard = TextWallMono(display, 0, 92, SCREEN_WIDTH - 20, 16)
        self.output = TextWallMono(display, 35, 40, 210, 32)
        self.instructions = TextWall(display, 5, 10, SCREEN_WIDTH - 25, 15)

    async def start(self, controller):
        # Setup inputs
        # inputManager.register(Input.A, controller.gotoMnemonicCreator)

        # Draw initial view
        display.pen(15)
        display.clear()
        self.controlsUI.render()

        self.keyboard.setFont("sans", 0.45)
        self.keyboard.setSpaceWidth(5)
        self.keyboard.setText("    0 1 2 3 4 5 6 7 8 9 A B C D E F")
        self.keyboard.render()

        self.output.setThickness(2)
        self.output.setFont("sans", 0.45)
        self.output.setSpaceWidth(5)
        self.output.setText("A5D EF1 400 A0_ ___ ___ A__ ___ ___ ___ ___ __  ")
        self.output.render()

        self.instructions.setText("Enter hexadecimal codes for your key:")
        self.instructions.render()

        display.rectangle(19, 100, 11, 2)

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
