'''Provar que os processos nao compartilham dados entre eles'''
import multiprocessing as mp
import time


def func1(val, stat):
    if stat:
        res = val+10
        stat = False
    else:
        res = val+20
        val = 200
        stat = True
    print(f'O resultado da função 1 é: {res}')  # Esperamos: 120
    time.sleep(0.001)


def func2(val, stat):
    if stat:
        res = val+30
        stat = False
    else:
        res = val+40
        val = 400
        stat = True
    print('')
    print(f'O resultado da função 2 é: {res}')  # Esperamos: 140
    time.sleep(0.001)


def main():
    valor = 100
    status = False

    p1 = mp.Process(target=func1, args=(valor, status))
    p2 = mp.Process(target=func2, args=(valor, status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
