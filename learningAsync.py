import asyncio
import time


async def fun1():
    print("started fun1")
    await asyncio.sleep(7)
    print("ended fun1")


async def fun2():
    print("started fun2")
    await asyncio.sleep(3)
    print("ended fun2")


async def main():
    s = time.time()
    a = asyncio.create_task(fun1())
    b = asyncio.create_task(fun2())
    await a
    await b
    print(f"took {time.time() - s} seconds")


asyncio.run(main())
