import datetime
import math
import asyncio


def main():
    print("Inicio da execução")
    inicio = datetime.datetime.now()
    el = asyncio.get_event_loop()
    # Forma1
    #el.run_until_complete(computar(inicio=1, fim=50_000_000))

    # Forma2
    tarefa1 = el.create_task(computar(inicio=1, fim=10_000_000))
    tarefa2 = el.create_task(computar(inicio=10_000_000, fim=20_000_000))
    tarefa3 = el.create_task(computar(inicio=20_000_000, fim=30_000_000))
    tarefa4 = el.create_task(computar(inicio=30_000_000, fim=40_000_000))
    tarefa5 = el.create_task(computar(inicio=40_000_000, fim=50_000_000))

    # Gather é o coletor de tarefas
    tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3, tarefa4, tarefa5)
    el.run_until_complete(tarefas)

    fim = datetime.datetime.now()
    result = fim - inicio
    print(f'Acabou execução em: {result}')


async def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos-fator)*(pos-fator))

if __name__ == '__main__':
    main()

"""
Forma1: Terminou em 17 segundos em média!
Forma2: Terminou em 17 segundos em média!
Ou seja nao mudou nada quebrar o processamento em tarefas, pois ela é async. 
"""
