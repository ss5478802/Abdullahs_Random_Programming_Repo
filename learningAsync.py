import asyncio


async def fun1():
    print("Function 1 started...")
    await asyncio.sleep(7)
    print("Function 1 ended!")


async def fun2():
    print("Function 2 started...")
    await asyncio.sleep(5)
    print("Function 2 ended!")


async def main():
    task1 = asyncio.create_task(fun1())
    task2 = asyncio.create_task(fun2())
    await task2
    await task1
    #await asyncio.gather(fun2(),fun1())


asyncio.run(main())
