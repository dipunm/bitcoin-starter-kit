import math

class TextWall:
    def __init__(self, display, anchor_x: int, anchor_y: int, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.display = display
        self.scrollRow = 0
        self.lineHeight = 15
        self.maxRow = math.floor(self.height / self.lineHeight)


    def setText(self, text):
        self.text = text

        self.lines = []
        lines = self.text.split('\n')
        print("lines: ", len(lines))
        row = 0
        col = 0
        for line in lines:
            words = line.split(" ")
            for word in words:
                toPrint = " " + word if col > 0 else word
                word_width = self.display.measure_text(toPrint)
                if col > 0 and word_width + col > self.width:
                    # Move to next line
                    row += 1
                    col = 0
                    toPrint = word
                print("LINES", len(self.lines), "ROW", row)
                if row >= len(self.lines): 
                    self.lines.append("")

                self.lines[row] += toPrint
                col += word_width
            col = 0
            row += 1
    
    def scrollUp(self):
        self.scrollRow = 0 if self.scrollRow < 1 else self.scrollRow - 1

    def scrollDown(self):
        self.scrollRow += 1 if len(self.lines) - self.maxRow - self.scrollRow - 1 > 0 else 0

    def clearSpace(self):
        self.display.pen(15)
        print("clearing::::", self.anchor_x, self.anchor_y, self.width, self.height)
        self.display.rectangle(self.anchor_x, self.anchor_y, self.width, self.height)
        self.display.pen(0)

    def render(self):
        self.clearSpace()

        for i in range(self.scrollRow, self.scrollRow + self.maxRow):
            if i >= len(self.lines):
                break

            self.display.text(
                self.lines[i], 
                self.anchor_x, 
                self.anchor_y + ((i - self.scrollRow) * self.lineHeight), 
                1
            )