# 02_async_await.py
# Advanced async programming with async/await and asyncio.

import asyncio

async def fetch_data(name, delay):
    print(f'Starting {name}')
    await asyncio.sleep(delay)
    print(f'Finished {name}')
    return f'Result {name}'


async def main():
    tasks = [fetch_data('A', 1), fetch_data('B', 2), fetch_data('C', 1.5)]
    results = await asyncio.gather(*tasks)
    print('Results:', results)


if __name__ == '__main__':
    asyncio.run(main())
