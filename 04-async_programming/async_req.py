import asyncio
import aiohttp
import time

async def fetchFromGoogle():
    url = 'https://www.google.com'
    session = aiohttp.ClientSession()
    resp = await session.get(url)
    await resp.content.read()
    await session.close()

async def main():
    print(time.strftime('%X'))
    await asyncio.gather(
        *[
            fetchFromGoogle() for _ in range (20)
        ]
        )
    # for _ in range(20):
    #     fetchFromGoogle() (these are synchronous requests, takes x4 times than it does ofr asynchronous requests)
     
        
    print(time.strftime('%X'))

if __name__ == '__main__':
    asyncio.run(main())
