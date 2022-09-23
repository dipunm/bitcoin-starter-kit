import uasyncio
from apps.mnemonic_creator.screens.dice_entropy_hex import DiceEntropyHexPage

async def main():
    step = DiceEntropyHexPage().start
    while True:
        step = await step()

uasyncio.run(main())