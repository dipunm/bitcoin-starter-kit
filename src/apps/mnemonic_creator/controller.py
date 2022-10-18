from apps.mnemonic_creator.helpers.die_to_hex import die_to_hex
from apps.mnemonic_creator.views.hex import HexView
from apps.mnemonic_creator.views.words import WordsView
from core.base.icontroller import IController
import apps.menu as menu
from apps.mnemonic_creator.views.diceboard import DiceBoardView
from core.base.iview import IView
from shared.views.text_summary import TextSummaryView

class MnemonicController(IController):
    async def run(self):
        self.view = TextSummaryView("""Let's roll!
        
        Dice rolls are a great source of randomness. Consider, after 142 rolls, what is the chances of anyone ever rolling the same 142 results in the same order ever again?! (hint: astronomically low, practically impossible)

        We will use the recorded roles to create a new Bitcoin private key! 
        
        Warning: Don't manipulate the results, even if you happen to roll the same number multiple times in a row; real random numbers don't always look completely random.

        After loading the next page, roll your dice and record each result by tapping the "count" button until you see the correct die face. Press the "next" button to enter the next result, and continue until you have entered enough results to continue (142 rolls).

        To continue to the next page, press OK.
        """, self.gotoDiceBoard)

        while (self.view):
            await self.view.start(self)
        
        # Return to menu when exiting.
        return menu.MenuController()

    async def gotoDiceBoard(self):
        size = 142
        self.dieRolls = [0] * size
        await self.change_view(DiceBoardView(self.dieRolls))

    async def submitEntropy(self):
        await self.change_view(TextSummaryView("""Showing the work

        The next page will present a summary of your dice rolls, alongside their corresponding 3 letter hex codes.

        Dice rolls in groups of 6 are mapped to 3 letter codes using [Lookup Table 1.1]
        
        Note: The last code will be missing one or two characters which will be filled later by a "checksum".

        Use the lookup table on page 3 of the guide to double check and verify the algorithm.

        To continue, press OK.
        """, self.showHex))

    async def showHex(self):
        self.hexCodes = die_to_hex(self.dieRolls)
        await self.change_view(HexView(self.dieRolls, self.hexCodes))

    async def explainChecksum(self):
        self.checksum = '5F'
        await self.change_view(TextSummaryView(f"""Checksum

        Your checksum is -> {self.checksum} <-

        The checksum completes the final 3 letter code. 
        
        A checksum acts like a digital tamper evident seal, like the stickers that leave "void" on a box when peeled off. When setting up or restoring a wallet, if any of the words are accidentally re-arranged, changed, or mistyped, a computer will use the checksum to detect it and prompt you to fix the mistake.

        Due to the complexity of the mathematics required to calculate a checksum, it is the only step that typically requires an electronic device to perform.

        To continue, press OK.
        """, self.explainWords))

    async def explainWords(self):
        self.checksum = '5F'
        await self.change_view(TextSummaryView(f"""Your mnemonic phrase

        The next page will show you your mnemonic phrase, write these words down securely and keep it private.
        
        This is your unique private key that only you and this device has ever seen.

        Below each word, you will see the 3 digit code used to pick it, you can verify each word was picked correctly using [Lookup Table 1.2].

        To continue, press OK.
        """, self.showWords))

    async def showWords(self):
        await self.change_view(WordsView(''.join(self.hexCodes) + self.checksum))

    async def exit(self):
        await self.change_view(False)

    async def change_view(self, view: IView | bool):
        old_view = self.view
        self.view = view
        if (old_view):
            await old_view.dispose()