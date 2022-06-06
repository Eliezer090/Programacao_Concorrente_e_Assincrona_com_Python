# Concorrencia em Processos
import multiprocessing as mp
import time


def processar():
    print('[', end='', flush=True)
    for _ in range(10):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)


if __name__ == '__main__':
    t1 = mp.Process(target=processar)
    t1.start()
    t1.join()
