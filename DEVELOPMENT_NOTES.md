- `ScreenUpdater`: Responsible for sending screen refresh commands in a separate thread. This allows us to have a more responsive feeling UX.
- `PageManager`: Keeps the application in an infinite loop and transitions from page to page. It also provides dependencies to each page. Each page is almost like its own application and must dictate what page to transition to when it exits.
- `InputManager`: Is basically like an observable, typically initialized and then started. It keeps the application idle while waiting for inputs and then triggers actions as registered. When stopped, the application's main function will resume, typically exiting the current page.


## Feature: Roll a mnemonic seed.
- Collect Dice rolls.
- Convert to HEX
- Convert to Words


We are going to do MVC

Controller -> Chooses View, Updates Model(s), Sends Model View
View -> Listens for IO, Calls Controller
Model -> (Data, BL)

Model: DiceBoard(12/24)
- IncDie(x)
- IsComplete()

View:
- EnableDone()
- RenderDie(x, n)
- MoveCursor(x)

Controller:
- Next
- Prev
- CycleDie
- Complete
- Exit