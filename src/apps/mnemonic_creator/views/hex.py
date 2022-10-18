from core.io.input_manager import Input
from core.presentation.text_wall_mono import TextWallMono
from core.io import display, inputManager, screenUpdater
import uasyncio
import badger2040


N_ROLLS_PER_WORD = 6
N_WORDS_PER_LINE = 6
N_HEX_PER_WORD = 3

class HexView:
    def __init__(self, die_chars, hex_chars) -> None:
        chunked_die_chars = [''.join(str(digit) for digit in die_chars[i:i + N_ROLLS_PER_WORD]) for i in range(0, len(die_chars), N_ROLLS_PER_WORD)]
        dieMsg = '\n\n'.join([' '.join(chunked_die_chars[i:i + N_WORDS_PER_LINE]) for i in range(0, len(chunked_die_chars), N_WORDS_PER_LINE)])
        
        chunked_hex_chars = [' '.join(str(digit) for digit in hex_chars[i:i + N_HEX_PER_WORD]) for i in range(0, len(hex_chars), N_HEX_PER_WORD)]
        hexMsg = '\n '+'\n\n '.join(['  '.join(chunked_hex_chars[i:i + N_WORDS_PER_LINE]) for i in range(0, len(chunked_hex_chars), N_WORDS_PER_LINE)])
        
        self.textwallrolls = TextWallMono(display, 18, 5, 267, 108)
        self.textwallrolls.setText(dieMsg)
        self.textwallhex = TextWallMono(display, 15, 3, 270, 110)
        self.textwallhex.setText(hexMsg)

    def prepareUI(self):        
        # Clear the UI areas
        display.pen(15)
        display.rectangle(0, 114, 296, 15)
        display.rectangle(287, 0, 10, 128)
        
        display.pen(0)
        display.line(0, 114, 287, 114)
        display.line(287, 0, 287, 115)

        display.pen(0)
        display.thickness(1)
        display.font("bitmap8")
        display.text("OK", 32, 118, 1)

    def clear(self):
        display.update_speed(badger2040.UPDATE_NORMAL)
        display.pen(15)
        display.clear()
        display.pen(0)
    
    async def start(self, controller):
        # Setup inputs
        inputManager.register(Input.A, controller.explainChecksum)

        # Draw initial view
        display.led(95)
        self.clear()
        self.prepareUI()
        self.textwallrolls.render()
        self.textwallhex.render(clearSpace=False)

        # Refresh screen
        screenUpdater.start()
        screenUpdater.QueueUpdate(delay_ms=0)
        await uasyncio.sleep_ms(50)
        
        # Configure for fast refreshes
        display.update_speed(
            badger2040.UPDATE_FAST
        )
        display.led(0)

        # Start input listener
        await inputManager.start()


    async def dispose(self):
        inputManager.stop()
        inputManager.reset()
        screenUpdater.stop()