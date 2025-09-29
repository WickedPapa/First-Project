#FUNZIONI SINCRONE e ASINCRONE
import asyncio
import time

def sincrona():
    print("3 - Inizio Sincrona")
    time.sleep(2)
    print("4 - Fine Sincrona")

async def asincrona():
    print("2 -Inizio Asincrona")
    await asyncio.sleep(2)
    print("6 - Fine Asincrona")

if __name__ == '__main__':
    print("1 - Inizio Main")
    asyncio.run(asincrona())
    sincrona()
    print("Fine Main")
