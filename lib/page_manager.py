from lib.input_manager import InputManager
from lib.screen_updater import ScreenUpdater
from pages import DiceEntropyPage

class PageManager:
    page: DiceEntropyPage
    def __init__(self, inputManager: InputManager, screenUpdater: ScreenUpdater) -> None:
        self.screen = screenUpdater
        self.inputs = inputManager

    async def start(self):
        self.page = DiceEntropyPage(self.inputs, self.screen)
        await self.page.start()