import asyncio
import time

TEMPO_BOLLITURA_ACQUA = 4
TEMPO_PREPARAZIONE_CONTIMENTO = 6
TEMPO_COTTURA_PASTA = 3

def fai_bollire_acqua_sync():
    print("FACCIO BOLLIRE ACQUA")
    time.sleep(TEMPO_BOLLITURA_ACQUA)
    print("ACQUA PRONTA")

def prepara_condimento_sync():
    print("PREPARO CONDIMENTO")
    time.sleep(TEMPO_PREPARAZIONE_CONTIMENTO)
    print("CONDIMENTO PRONTO")

def cuoci_pasta_sync():
    fai_bollire_acqua_sync()
    print("PREPARO PASTA")
    time.sleep(TEMPO_COTTURA_PASTA)
    print("CONDIMENTO PRONTO")

def prepara_pasta_sync():
    start = time.time()
    prepara_condimento_sync()
    cuoci_pasta_sync()
    end = time.time()
    elapsed = end - start
    print(f"Tempo preparazione SYNC {elapsed:.2f} seconds")

##################################################################
async def fai_bollire_acqua_async():
    print("FACCIO BOLLIRE ACQUA")
    await asyncio.sleep(TEMPO_BOLLITURA_ACQUA)
    print("ACQUA PRONTA")

async def prepara_condimento_async():
    print("PREPARO CONDIMENTO")
    await asyncio.sleep(TEMPO_PREPARAZIONE_CONTIMENTO)
    print("CONDIMENTO PRONTO")

async def cuoci_pasta_async():
    await fai_bollire_acqua_async()
    print("PREPARO PASTA")
    await asyncio.sleep(TEMPO_COTTURA_PASTA)
    print("PASTA PRONTA")

async def prepara_pasta_async():
    start = time.time()
    await asyncio.gather(cuoci_pasta_async(), prepara_condimento_async())
    end = time.time()
    elapsed = end - start
    print(f"Tempo preparazione ASYNC {elapsed:.2f} seconds")

##################################################################

if __name__ == '__main__':
    print("SYNC")
    prepara_pasta_sync()
    print("\nASYNC")
    asyncio.run(prepara_pasta_async())