from core.base.iview import IView
from core.consts import SCREEN_HEIGHT, SCREEN_WIDTH
from core.io import inputManager, display, screenUpdater
from core.io.input_manager import Input
import badger2040
from core.presentation.controls_bar import ControlsBar
from core.presentation.text_wall import TextWall

from core.presentation.text_wall_mono import TextWallMono

class WordsView(IView):
    def __init__(results) -> None:
        pass

    async def start(self, controller):
        pass

    async def dispose(self):
        pass