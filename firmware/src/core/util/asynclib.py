import uasyncio

def createLinker(tasks):
    def link(task):
        async def fn():
            result = await task
            for i in range(len(tasks)):
                if tasks[i] == task:
                    continue
                tasks[i].cancel()
            return result
        return fn()
    return link
    

async def oneOf(*coroutines):
    tasks = list(map(uasyncio.create_task, coroutines))
    linkTo = createLinker(tasks)
    linked = list(map(linkTo, tasks))
    results = await uasyncio.gather(*linked, return_exceptions=True)
    result = next(x for x in results if not type(x) == uasyncio.CancelledError)
    return result
  