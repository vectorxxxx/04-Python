import asyncio
import threading


async def hello():
    print('Hello World! (%s)' % threading.current_thread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(hello()), asyncio.ensure_future(hello())]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
