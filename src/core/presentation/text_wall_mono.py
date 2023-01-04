import math
from badger2040 import Badger2040

class TextWallMono:
    def __init__(self, display: Badger2040, anchor_x: int, anchor_y: int, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.display = display
        self.scrollRow = 0
        self.lineHeight = 16
        self.maxRow = math.floor(self.height / self.lineHeight)
        self.font = "bitmap8"
        self.size = 1
        self.space_width = None
        self.thickness = 1

    def setSpaceWidth(self, width=None):
        self.space_width = width

    def setThickness(self, thickness=1):
        self.thickness = thickness

    def setFont(self, font: str, size=1):
        self.font = font
        self.size = size

    def setText(self, text: str):
        self.text = text

        self.display.font(self.font)
        self.letter_width = self.display.measure_text("M", self.size)
        space_width = self.letter_width if self.space_width == None else self.space_width

        self.lines = []
        lines = self.text.split('\n')
        row = 0
        col = 0
        for line in lines:
            if row >= len(self.lines):
                self.lines.append("")

            for letter in line:
                width = space_width if letter == " " else self.letter_width
                if col > 0 and width + col > self.width:
                    # Move to next line
                    row += 1
                    col = 0

                if row >= len(self.lines):
                    self.lines.append("")

                self.lines[row] += letter
                col += width
            col = 0
            row += 1

    def canScrollUp(self):
        return self.scrollRow > 0

    def canScrollDown(self):
        return len(self.lines) - self.maxRow - self.scrollRow - 1 > 0

    def scrollUp(self):
        if self.canScrollUp():
            self.scrollRow -= min(self.maxRow, self.scrollRow)

    def scrollDown(self):
        if self.canScrollDown():
            self.scrollRow += min(
                self.maxRow - 1,
                len(self.lines) - self.scrollRow - self.maxRow - 1
            )

    def clearSpace(self):
        self.display.pen(15)
        self.display.rectangle(
            self.anchor_x, self.anchor_y, self.width, self.height)
        self.display.pen(0)

    def render(self, clearSpace=True):
        if clearSpace:
            self.clearSpace()

        space_width = self.letter_width if self.space_width == None else self.space_width

        self.display.pen(0)
        self.display.thickness(self.thickness)
        for row in range(self.scrollRow, self.scrollRow + self.maxRow):
            if row >= len(self.lines):
                break

            cursor_x = 0
            for letter in range(0, len(self.lines[row])):
                self.display.text(
                    self.lines[row][letter],
                    self.anchor_x + cursor_x,
                    self.anchor_y + ((row - self.scrollRow) * self.lineHeight),
                    self.size
                )
                cursor_x += space_width if self.lines[row][letter] == " " else self.letter_width
