from core.base.iview import IView
from core.consts import SCREEN_HEIGHT, SCREEN_WIDTH
from core.io import inputManager, display, screenUpdater
from core.io.input_manager import Input
import badger2040
from core.presentation.controls_bar import ControlsBar
from core.presentation.text_wall import TextWall

from core.presentation.text_wall_mono import TextWallMono

class ResultsView(IView):
    def __init__(self, codes: list[str], result: str, fingerprint: str):
        codesStr = " ".join(["".join((codes + [result])[i:i+3]) for i in range(0, 36, 3)])
        self.result = result
        
        self.instructions1 = TextWall(display, 17, 14, 87, 15)
        self.instructions2 = TextWall(display, 155, 14, 84, 15)
        self.instructions3 = TextWall(display, 155, 59, 84, 15)
        self.codesWall = TextWallMono(display, 22, 34, 10*4*3, 64)
        self.codesWall.setText(codesStr)
        self.fingerprint = TextWallMono(display, 176, 81, 10*8, 16)
        self.fingerprint.setText(fingerprint)        
        self.controlsUI = ControlsBar(display, A="DISCARD", B="WORDS", C="SAVE")

    async def start(self, controller):
        # Setup inputs
        inputManager.register(Input.A, controller.discard)
        inputManager.register(Input.B, controller.show_words)

        display.pen(15)
        display.clear()

        display.pen(0)
        display.thickness(2)
        self.drawBox([12, 15, 130, 82])
        self.drawBox([152, 15, 130, 36])
        self.drawBox([152, 61, 130, 36])

        self.instructions1.setText(" Hex codes:")
        self.instructions1.render()

        self.instructions2.setText(" Checksum:")
        self.instructions2.render()

        self.instructions3.setText(" Fingerprint:")
        self.instructions3.render()

        self.codesWall.setThickness(2)
        self.codesWall.setFont("sans", 0.45)
        self.codesWall.resetText()
        self.codesWall.render(clearSpace=False)

        self.fingerprint.setThickness(2)
        self.fingerprint.setFont("sans", 0.45)
        self.fingerprint.resetText()
        self.fingerprint.render(clearSpace=False)

        self.controlsUI.render()

        display.thickness(2)
        display.font("sans")
        display.text(self.result, 210, 35, 0.7)

        # Update screen
        screenUpdater.start()
        screenUpdater.QueueUpdate()

        # Configure for fast refreshes
        display.update_speed(badger2040.UPDATE_FAST)

        # Start input listener
        await inputManager.start()

    def drawBox(self, box):
        display.line(box[0], box[1], box[0] + box[2], box[1])
        display.line(box[0], box[1], box[0], box[1] + box[3])
        display.line(box[0] + box[2], box[1], box[0] + box[2], box[1] + box[3])
        display.line(box[0], box[1] + box[3], box[0] + box[2], box[1] + box[3])

    async def dispose(self):
        inputManager.stop()
        screenUpdater.stop()
        inputManager.reset()
