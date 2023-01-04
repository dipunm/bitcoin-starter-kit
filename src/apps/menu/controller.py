from apps.menu.views.view import MenuView
import apps.mnemonic_creator as mnemonic_creator
import apps.checksum as checksum
from core.base.icontroller import IController


class MenuController(IController):
    async def run(self):
        self.view = MenuView()
        await self.view.start(self)
        return self.next

    async def gotoMnemonicCreator(self):
        self.next = mnemonic_creator.MnemonicController()
        await self.view.dispose()

    async def gotoChecksum(self):
        self.next = checksum.ChecksumController()
        await self.view.dispose()
