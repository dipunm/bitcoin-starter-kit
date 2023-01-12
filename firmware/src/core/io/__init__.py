import badger2040 as __badger2040
from core.io.input_manager import InputManager as __InputManager
from core.io.screen_updater import ScreenUpdater as __ScreenUpdater

display = __badger2040.Badger2040()
screenUpdater = __ScreenUpdater(display)
inputManager = __InputManager()