import asyncio
import selectors


import time

async def a():

    print("Start a()")
    await asyncio.sleep(3)
    print("End a()")


async def b():
    print('start b()')
    await asyncio.sleep(2)
    print('end b()')

async def main():

    # s = asyncio.create_task(a())
    # s1 = asyncio.create_task(b())
    #
    # await s
    # await s1

    await asyncio.gather(
        a(),
        b()
    )

if __name__ == '__main__':
    asyncio.run(main())