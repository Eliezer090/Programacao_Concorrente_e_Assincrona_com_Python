# Versao com a solução do problema, demora mais mas os dados consistem no final
import multiprocessing
import datetime


def depositar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value + 1


def sacar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value - 1


def realizar_transacao(saldo, lock):
    pc1 = multiprocessing.Process(target=depositar, args=(saldo, lock,))
    pc2 = multiprocessing.Process(target=sacar, args=(saldo, lock,))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


if __name__ == '__main__':
    saldo = multiprocessing.Value('i', 100)
    inicio = datetime.datetime.now()
    print(f'Saldo inicial: {saldo.value}')
    lock = multiprocessing.RLock()
    for _ in range(10):
        realizar_transacao(saldo, lock)
    fim = datetime.datetime.now()
    print(f'Saldo final: {saldo.value}')
    print(f'Terminou em {fim-inicio}')
