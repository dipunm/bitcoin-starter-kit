from consts.PageAliases import Aliases
from pages import DiceEntropyPage, MenuPage, DiceEntropyInfoPage, DiceEntropyHexPage
from lib.input_manager import InputManager
from lib.screen_updater import ScreenUpdater

class PageManager:
    def __init__(self, inputManager: InputManager, screenUpdater: ScreenUpdater) -> None:
        self.screen = screenUpdater
        self.inputs = inputManager
        self.pages = {
            Aliases.menu: lambda : MenuPage(inputManager, screenUpdater),
            Aliases.dice_entropy: lambda : DiceEntropyPage(inputManager, screenUpdater),
            Aliases.dice_entropy_info: lambda : DiceEntropyInfoPage(inputManager, screenUpdater),
            Aliases.dice_entropy_hex: lambda : DiceEntropyHexPage(inputManager, screenUpdater),
        }

    async def start(self):
        self.page = DiceEntropyHexPage(self.inputs, self.screen)
        while True:
            nextPage = await self.page.start()
            self.page = self.pages[nextPage]()