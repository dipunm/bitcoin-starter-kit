def drawIndicator(display, pos):
    _x = (pos % 19)
    _y = (pos-_x)/19
    x = int(15 * _x) + 1
    y = int(15 * _y) + 1
    display.pen(0)
    display.rectangle(x,y+16,14,3)
    
def drawDice(display, pos, val):
    _x = (pos % 19)
    _y = (pos-_x)/19
    x = int(15 * _x) + 1
    y = int(15 * _y) + 1
    display.pen(0)
    display.rectangle(x-1,y-1,16,16)
    display.pen(15)
    display.rectangle(x,y,14,14)
    display.pen(0)
    if val == 1:
        display.rectangle(x+6,y+6,2,2)
    elif val == 2:
        display.rectangle(x+2,y+2,2,2)
        display.rectangle(x+10,y+10,2,2)
    elif val == 3:
        display.rectangle(x+2,y+2,2,2)
        display.rectangle(x+6,y+6,2,2)
        display.rectangle(x+10,y+10,2,2)
    elif val == 4:
        display.rectangle(x+2,y+2,2,2)
        display.rectangle(x+2,y+10,2,2)
        display.rectangle(x+10,y+2,2,2)
        display.rectangle(x+10,y+10,2,2)
    elif val == 5:
        display.rectangle(x+2,y+2,2,2)
        display.rectangle(x+2,y+10,2,2)
        display.rectangle(x+10,y+2,2,2)
        display.rectangle(x+10,y+10,2,2)
        display.rectangle(x+6,y+6,2,2)
    elif val == 6:
        display.rectangle(x+2,y+2,2,2)
        display.rectangle(x+2,y+6,2,2)
        display.rectangle(x+2,y+10,2,2)      
        display.rectangle(x+10,y+2,2,2)
        display.rectangle(x+10,y+6,2,2)
        display.rectangle(x+10,y+10,2,2)
