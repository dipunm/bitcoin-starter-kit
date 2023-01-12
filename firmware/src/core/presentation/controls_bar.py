from badger2040 import Badger2040

from core.consts import SCREEN_HEIGHT, SCREEN_WIDTH

class ControlsBar:
    def __init__(self, display: Badger2040, A = None, B = None, C = None, UP = None, DOWN = None) -> None:
        self.display = display
        self.A = A
        self.B = B
        self.C = C
        self.UP = UP
        self.DOWN = DOWN

    def drawBottom(self, pos, text):
        if text == None:
            return
        
        self.display.font("bitmap8")
        self.display.thickness(1)
        scale = 1
        yoffset = 9
        y = SCREEN_HEIGHT - 20 + yoffset
        x_box = SCREEN_WIDTH/3
        x_txt_len = self.display.measure_text(text, scale)
        offset = (pos - 1) * x_box
        x = 0 if x_txt_len > x_box else (x_box - x_txt_len)/2 + offset
        self.display.text(text, int(round(x)), y, scale)

    def drawSide(self, pos, text):
        if text == None:
            return
        
        self.display.font("bitmap8")
        self.display.thickness(1)
        scale = 1
        xoffset = 6
        # bitmap8 = 8px high
        yoffset = 8 / 2 * scale
        x = SCREEN_WIDTH - 20 + xoffset
        y = SCREEN_HEIGHT / 4 + SCREEN_HEIGHT / 2 * (pos - 1) - yoffset - 3
        self.display.text(text, x, int(round(y)), scale)

    def render(self):
        self.display.thickness(1)
        if (self.A != None or self.B != None or self.C != None):
            self.display.pen(15)
            self.display.rectangle(0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20)
            self.display.pen(0)
            self.display.line(0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, SCREEN_HEIGHT - 20)
            self.drawBottom(1, self.A)
            self.drawBottom(2, self.B)
            self.drawBottom(3, self.C)

        if (self.UP != None or self.DOWN != None):
            self.display.pen(15)
            self.display.rectangle(SCREEN_WIDTH - 20, 0, 20, SCREEN_HEIGHT - 19)
            self.display.pen(0)
            self.drawSide(1, self.UP)
            self.drawSide(2, self.DOWN)
            self.display.line(SCREEN_WIDTH - 20, 0, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)

