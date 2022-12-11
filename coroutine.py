import asyncio

async def coro():
    while True:
        print("hi")
        await asyncio.sleep(1)

async def coro2():
    while True:
        print("hello")
        await asyncio.sleep(1)
async def main():
    while True:
        coro()
        coro2()
        await asyncio.sleep(0.1)

asyncio.run(main())