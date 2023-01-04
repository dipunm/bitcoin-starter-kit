from apps.checksum.views.data_input_view import DataInputView
from core.base.icontroller import IController


class ChecksumController(IController):
    async def run(self):
        self.view = DataInputView()
        await self.view.start(self)
        return self.next
