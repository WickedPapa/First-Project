import asyncio
import time

async def prepara_caffe():
    print("Preparing Caffe")
    await asyncio.sleep(2)
    print("Caffe is ready")

async def riscalda_latte():
    print("Preparing Milk")
    await asyncio.sleep(3)
    print("Milk is ready")

def prepara_schiuma_e_termina():
    print("Preparing Schiuma")
    time.sleep(2)
    print("Schiuma is ready")
    print("Preparing Cappucino")
    time.sleep(1)
    print("Cappucino is ready")

async def prepara_cappucino():
    start = time.time()
    await asyncio.gather(prepara_caffe(), riscalda_latte()) #aggiungo le chiamate al pool delle chiamate da fare in parallelo
    prepara_schiuma_e_termina()
    end = time.time()
    elapsed = end - start
    print(f"Tempo preparazione ASYNC {elapsed:.2f} seconds")

if __name__ == '__main__':
    asyncio.run(prepara_cappucino())