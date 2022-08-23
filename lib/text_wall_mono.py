import math

class TextWallMono:
    def __init__(self, display, anchor_x: int, anchor_y: int, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.display = display
        self.scrollRow = 0
        self.lineHeight = 14
        self.maxRow = math.floor(self.height / self.lineHeight)


    def setText(self, text):
        self.text = text

        self.display.pen(0)
        self.display.thickness(1)
        self.display.font("bitmap8")
        self.letter_width = self.display.measure_text("M",1)

        self.lines = []
        lines = self.text.split('\n')
        row = 0
        col = 0
        for line in lines:
            if row >= len(self.lines): 
                self.lines.append("")

            for letter in line:
                toPrint = letter
                word_width = len(toPrint) * self.letter_width
                if col > 0 and word_width + col > self.width:
                    # Move to next line
                    row += 1
                    col = 0
                    toPrint = letter
                
                if row >= len(self.lines): 
                    self.lines.append("")

                self.lines[row] += toPrint
                col += word_width
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
        self.display.rectangle(self.anchor_x, self.anchor_y, self.width, self.height)
        self.display.pen(0)

    def render(self, clearSpace=True):
        if clearSpace:
            self.clearSpace()

        for i in range(self.scrollRow, self.scrollRow + self.maxRow):
            if i >= len(self.lines):
                break

            for l in range(0, len(self.lines[i])):
                self.display.text(
                    self.lines[i][l],
                    self.anchor_x + (l * self.letter_width),
                    self.anchor_y + ((i - self.scrollRow) * self.lineHeight), 
                    1    
                )
