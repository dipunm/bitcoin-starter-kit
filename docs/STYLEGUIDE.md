# Style Guide

## Framework
This project has been designed around the MVC pattern in an attempt to create a familiar project structure and separation of concerns.

The file structure is designed to scale, using feature folders (`apps`) to group related components together instead treating the whole project as a single monolithic application.

## Folder structure
The folder structure briefly follows:

- src
    - main.py: The entry file for the application
    - apps: this folder contains packaged features
        - [feature]
            - \_\_init__.py: A convenience file, use to export entities that are accessed by other features or by the main application.
            - controller.py: So far, each feature has a single controller, but this is not mandatory
            - views: A collection of the various views used by the feature.

    - core: contains common classes and features, the structure internally is a work in progress.

## Controllers, Views, and the InputManager
Controllers extend `core.base.icontroller.IController` which provides an async `run` method. This method should initialize and start a view, passing itself as a parameter.

```py
self.view = MyView()
await self.view.start(self)
```

The view (which should extend `core.base.iview.IView`) will configure and start the `InputManager` which will leave the application in an idle state, while calling the configured callback methods when configured buttons are pressed. Note that all callback methods should be async methods.

```py
inputManager.register(Input.A, controller.doSomething)
inputManager.register(Input.B, controller.doSomethingElse)

# Start input listener
await inputManager.start()
```

In order to transition to another controller or another view, the application will need to reactivate from its idle state. To do so requires calling `inputManager.stop()` which will typically be defined in `view.dispose()` which can be called by one of the callback methods in the controller.

This will resume the controller's `run` method; if you wish to switch to a different view, you can initialize and `start()` the appropriate view, however if you wish to switch to a different controller, you should initialize and return the relevant controller:

```py
async def run():
    # ... init code ...
    await self.view.start()
    # Continue from here...
    
    # Custom code: Switch to another view if appropriate.
    while True:
        self.view = self.getNextView()
        if (not self.view):
            break
        
        await self.view.start()

    # Alternatively return an alternative controller to run next
    # In this case, we return to the menu application
    return menu.MenuController()
```

## Circular dependencies
To avoid circular dependencies, it is recommended that controllers reference each other indirectly.

Instead of importing a controller like:
```py
from apps.menu import MenuController

# ..... initializing the controller:
controller = MenuController()
```

It should be referenced as follows:
```py
import apps.menu as menu

# ..... initializing the controller:
controller = menu.MenuController()
```

This will prevent circular dependency errors caused by two or more controllers transitioning between one another.

## View and Controller responsibilities
The view is responsible for:
- positioning and drawing elements on screen
- configuring, starting and stopping the inputManager

Technically, business logic and page state can live here, however it is encouraged to move business logic at bare minimum out into the controller and if necessary, to create models, services and helpers that are used by the controller to manage page state.

While prototyping, it can be useful to manage state within the view, however consider refactoring after.

