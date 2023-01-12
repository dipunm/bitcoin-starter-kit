from apps.checksum.views.data_input_view import DataInputView
from apps.checksum.views.results_view import ResultsView
from apps.checksum.views.words_view import WordsView
import apps.menu as menu
from core.base.icontroller import IController
from core.base.iview import IView
from core.crypto.hexCode import hex_to_checksum


class ChecksumController(IController):
    async def run(self):
        self.view = DataInputView()

        while (self.view):
            await self.view.start(self)

        return self.next

    async def showResults(self, data: list[str]):
        result = hex_to_checksum(data)
        fingerprint = "F00DBAB3"
        self.hex = data + [result]
        await self.change_view(ResultsView(data, result, fingerprint))

    async def discard(self):
        self.next = menu.MenuController()
        await self.change_view(False)

    async def show_words(self):
        await self.change_view(WordsView())

    async def change_view(self, view: IView | bool):
        old_view = self.view
        self.view = view
        if (old_view):
            await old_view.dispose()
