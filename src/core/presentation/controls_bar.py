from badger2040 import Badger2040

from core.consts import SCREEN_HEIGHT, SCREEN_WIDTH

class TextWallMono:
    def __init__(self, display: Badger2040, A = None, B = None, C = None, UP = None, DOWN = None) -> None:
        self.display = display
        self.A = A
        self.B = B
        self.C = C
        self.UP = UP
        self.DOWN = DOWN

    def drawBottom(self, pos, text):
        pass

    def drawSide(self, pos, text):
        pass

    def render(self):
        if (self.A != None or self.B != None or self.C != None):
            self.display.rectangle(0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20)
            self.drawBottom(1, self.A)
            self.drawBottom(2, self.B)
            self.drawBottom(3, self.C)
            self.display.partial_update(0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20)

        if (self.UP != None or self.DOWN != None):
            self.display.rectangle(SCREEN_WIDTH - 20, 0, 20, SCREEN_HEIGHT)
            self.drawSide(1, self.UP)
            self.drawSide(2, self.DOWN)
            self.display.partial_update(SCREEN_WIDTH - 20, 0, 20, SCREEN_HEIGHT)