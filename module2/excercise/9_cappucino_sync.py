import time

def prepara_caffe():
    print("Preparing Caffe")
    time.sleep(2)
    print("Caffe is ready")

def riscalda_latte():
    print("Preparing Milk")
    time.sleep(3)
    print("Milk is ready")

def prepara_schiuma_e_termina():
    print("Preparing Schiuma")
    time.sleep(2)
    print("Schiuma is ready")
    print("Preparing Cappucino")
    time.sleep(1)
    print("Cappucino is ready")

def prepara_cappucino():
    start = time.time()
    prepara_caffe()
    riscalda_latte()
    prepara_schiuma_e_termina()
    end = time.time()
    elapsed = end - start
    print(f"Tempo preparazione SYNC {elapsed:.2f} seconds")

if __name__ == '__main__':
    prepara_cappucino()