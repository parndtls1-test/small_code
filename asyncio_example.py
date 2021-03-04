import asyncio

async def dothis(stime):
    print(f'{stime} started')
    await asyncio.sleep(stime)
    print(f'{stime} ended')
    return

async def main():
    a1 = loop.create_task(dothis(15))
    a2 = loop.create_task(dothis(10))
    a3 = loop.create_task(dothis(5))
    await asyncio.wait([a1, a2, a3])
    return a1, a2, a3

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception as e:
        print(e)
    finally:
        loop.close()
