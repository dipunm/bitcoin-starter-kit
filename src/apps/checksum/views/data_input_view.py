from core.consts import SCREEN_HEIGHT, SCREEN_WIDTH
from core.io import display, inputManager, screenUpdater
from core.io.input_manager import Input
from core.base.iview import IView
import badger2040
from core.io.screen_updater import UpdateBox

from core.presentation.controls_bar import ControlsBar
from core.presentation.text_wall import TextWall
from core.presentation.text_wall_mono import TextWallMono
from core.tracking.counter import Counter


class DataInputView(IView):
    def __init__(self) -> None:
        self.controlsUI = ControlsBar(
            display, A="<=", B="=>", C="Select")
        # self.keyboard = TextWallMono(display, 20, 92, SCREEN_WIDTH - 40, 16)
        # self.output = TextWallMono(display, 35, 40, 210, 32)
        # self.instructions = TextWall(display, 5, 10, SCREEN_WIDTH - 25, 15)
        self.keyboard = TextWallMono(display, SCREEN_WIDTH - 20, 20, 11, SCREEN_HEIGHT - 40)
        self.output = TextWallMono(display, 35, 20, 105, 64)
        # self.instructions = TextWall(display, 5, 10, SCREEN_WIDTH - 25, 15)
        self.keyboardPos = Counter(0, 15, True)
        self.keyboardKeys = [hex(i)[-1].upper() for i in range(0, 16)]
        self.outputData = []

    async def keyboardLeft(self):
        self.keyboardPos.decrement()
        self.drawKeyboardIndicator()

    async def keyboardRight(self):
        self.keyboardPos.increment()
        self.drawKeyboardIndicator()

    async def keyboardSelect(self):
        if len(self.outputData) > 34:
            return
        
        self.outputData.append(self.keyboardKeys[self.keyboardPos.get()])
        self.drawOutputText()

    async def keyboardDel(self):
        if len(self.outputData) > 0:
            self.outputData.pop()
            self.drawOutputText()

    def drawKeyboardIndicator(self, queue=True):
        dx = 15
        offset = self.keyboardPos.get() * dx
        display.pen(15)
        display.rectangle(19, 100, dx * 16, 2)
        display.pen(0)
        display.rectangle(19 + offset, 100, 11, 2)
        if queue:
            screenUpdater.QueueUpdate()

    def drawOutputText(self, queue=True):
        chars = self.outputData + (["_"]*max(0, (35 - len(self.outputData))))
        text = " ".join(["".join(chars[i:i+3]) for i in range(0, 35, 3)])
        self.output.setText(text)
        self.output.render()
        if queue:
            screenUpdater.QueueUpdate(delay_ms=0)

    async def keyboardDown(self):
        print("noticedown")
        self.keyboardPos.increment()
        if self.keyboard.canScrollDown():
            self.keyboard.scrollDown()
        else:
            self.keyboard.scrollTop()
        self.keyboard.render()
        screenUpdater.QueuePartialUpdate(UpdateBox(
            x=self.keyboard.anchor_x, 
            y=self.keyboard.anchor_y, 
            w=self.keyboard.width, 
            h=self.keyboard.height
        ), delay_ms=10)

    async def keyboardUp(self):
        self.keyboardPos.decrement()
        if self.keyboard.canScrollUp():
            self.keyboard.scrollUp()
        else:
            self.keyboard.scrollEnd()
        
        self.keyboard.render()
        screenUpdater.QueuePartialUpdate(UpdateBox(
            x=self.keyboard.anchor_x, 
            y=self.keyboard.anchor_y, 
            w=self.keyboard.width, 
            h=self.keyboard.height
        ), delay_ms=10)

    async def start(self, controller):
        # Setup inputs
        inputManager.register(Input.A, self.keyboardLeft)
        inputManager.register(Input.B, self.keyboardRight)
        inputManager.register(Input.C, self.keyboardSelect)
        inputManager.register(Input.DOWN, self.keyboardDown)
        inputManager.register(Input.UP, self.keyboardUp)

        # Draw initial view
        display.pen(15)
        display.clear()
        self.controlsUI.render()

        self.keyboard.setFont("sans", 0.45)
        self.keyboard.setText("  0123456789ABCDEF   ")
        self.keyboard.render()

        self.output.setThickness(2)
        self.output.setFont("sans", 0.45)
        self.output.setSpaceWidth(5)
        self.drawOutputText(queue=False)

        # Draw input indicator
        ycenter = int(round(SCREEN_HEIGHT / 2)) - 12
        xstart = SCREEN_WIDTH - 8
        display.pixel(xstart, ycenter)
        display.pixel(xstart+1, ycenter)
        display.pixel(xstart+1, ycenter-1)
        display.pixel(xstart+1, ycenter+1)
        display.pixel(xstart+2, ycenter)
        display.pixel(xstart+2, ycenter-1)
        display.pixel(xstart+2, ycenter+1)
        display.pixel(xstart+2, ycenter-2)
        display.pixel(xstart+2, ycenter+2)
        display.pixel(xstart+3, ycenter)
        display.pixel(xstart+3, ycenter-1)
        display.pixel(xstart+3, ycenter+1)
        display.pixel(xstart+3, ycenter-2)
        display.pixel(xstart+3, ycenter+2)
        display.pixel(xstart+3, ycenter-3)
        display.pixel(xstart+3, ycenter+3)


        # self.instructions.setText("Enter hexadecimal codes for your key:")
        # self.instructions.render()

        # self.drawKeyboardIndicator(queue=False)

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
