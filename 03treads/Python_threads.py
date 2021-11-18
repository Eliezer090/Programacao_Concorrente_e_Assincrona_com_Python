import datetime
import math

import threading
import multiprocessing


def main():
    # Pega quantos cores tem o processador
    qtdCores = multiprocessing.cpu_count()
    print(f'realizando o processamento com {qtdCores} cores')

    inicio = datetime.datetime.now()

    threads = []
    # Percorre todos os cores do processador e distribui a tarefa
    for n in range(1, qtdCores+1):
        ini = 50_000_000 * (n-1)/qtdCores
        fim = 50_000_000 * n / qtdCores
        print(f'core {n} processando de {ini} ate {fim}')
        threads.append(threading.Thread(target=computar, kwargs={
                       'inicio': ini, 'fim': fim}, daemon=True))
    [th.start() for th in threads]
    [th.join() for th in threads]
    tempo = datetime.datetime.now() - inicio
    print(f'Terminou em {tempo.total_seconds():.2f} segundos!')


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000*1000
    while pos < fim:
        pos += 1
        math.sqrt((pos-fator)*(pos-fator))


if __name__ == '__main__':
    main()

# Terminou em 16.00 segundos!
