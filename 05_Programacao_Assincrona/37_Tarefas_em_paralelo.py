# 37. Exercício Prático: Executando Tarefas em Paralelo
# Uma obs, nao executa mais rapido do que o da aula 36, simplesmente é outra maneira de fazer a mesma coisa
import datetime
import asyncio


async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde a geração de {quantidade} dados')
    for i in range(quantidade):
        item = i * i
        await dados.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)
    print('Fim da geração de dados')


async def processar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde o processamento de {quantidade} dados')
    processados = 0
    while processados < quantidade:
        await dados.get()
        processados += 1
    print('Fim do processamento de dados')


def main():
    total = 5_000
    dados = asyncio.Queue()
    print(f'Computando {total*2:.2f} dados')

    el = asyncio.get_event_loop()
    tarefa1 = el.create_task(gerar_dados(total, dados))
    tarefa2 = el.create_task(gerar_dados(total, dados))
    tarefa3 = el.create_task(processar_dados(total*2, dados))
    # Gather é o coletor de tarefas
    tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3)
    el.run_until_complete(tarefas)


if __name__ == '__main__':
    main()
