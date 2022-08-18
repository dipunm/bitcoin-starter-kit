from lib.screen_updater import ScreenUpdater
from lib.input_manager import InputManager
from lib.page_manager import PageManager
import uasyncio
import badger2040

display = badger2040.Badger2040()
screenUpdater = ScreenUpdater(display)
inputManager = InputManager()
pageManager = PageManager(inputManager, screenUpdater)

uasyncio.run(pageManager.start())