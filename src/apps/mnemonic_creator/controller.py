from apps.mnemonic_creator.views.introduction import IntroductionView
from core.base.icontroller import IController
import apps.menu as menu
from apps.mnemonic_creator.views.diceboard import DiceBoardView

class MnemonicController(IController):
    async def run(self):
        self.view = IntroductionView("""Dice entropy
        
        Dice rolls are a great source of entropy. 142 rolls will allow us to generate 256bits of entropy in a verifiable way. Visit https://www.dipunmistry.co.uk/... for more details.

        After each die roll, press the 'count' button the appropriate number of times to record the dice roll, and then press the 'next' button to progress to the next record.

        To continue, press OK
        """)

        while (self.view):
            await self.view.start(self)
        
        return menu.MenuController()

    async def gotoDiceBoard(self):
        oldView = self.view
        self.view = DiceBoardView(142)
        await oldView.dispose()

    async def submitEntropy(self):
        pass

    async def exit(self):
        oldView = self.view
        self.view = False # No view will exit the app
        await oldView.dispose()
