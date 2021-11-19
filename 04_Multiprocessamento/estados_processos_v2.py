'''Compartilhar dados entre os 2 processos, 
    sem utilizar pipe ou queue, dados compartilhado em memoria é mais rapido'''
import multiprocessing as mp
import time
import ctypes


def func1(val, stat):
    # Precisamos botar o .value para pegar e setar o valor ao usar o ctypes
    if stat.value:
        res = val.value+10
        stat.value = False
    else:
        res = val.value+20
        val.value = 200
        stat.value = True
    print(f'O resultado da função 1 é: {res}')  # Esperamos: 120
    time.sleep(0.001)


def func2(val, stat):
    if stat.value:
        res = val.value+30
        stat.value = False
    else:
        res = val.value+40
        val.value = 400
        stat.value = True
    print('')
    print(f'O resultado da função 2 é: {res}')  # Esperamos: 230
    time.sleep(0.001)


def main():
    # Muda somente a forma que declaramos os valores para as variaveis
    valor = mp.Value('i', 100)
    status = mp.Value(ctypes.c_bool, False)

    p1 = mp.Process(target=func1, args=(valor, status))
    p2 = mp.Process(target=func2, args=(valor, status))

    p1.start()
    p1.join()

    p2.start()
    p2.join()


if __name__ == '__main__':
    main()
