from apps.menu.controller import MenuController
import uasyncio

async def main():
    controller = MenuController()
    while True:
        controller = await controller.run()

uasyncio.run(main())