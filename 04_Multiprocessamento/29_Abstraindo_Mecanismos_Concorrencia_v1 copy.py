# Concorrencia em threading
import threading
import time


def processar():
    print('[', end='', flush=True)
    for _ in range(10):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)


if __name__ == '__main__':
    t1 = threading.Thread(target=processar)
    t1.start()
    t1.join()
