# 36. Exercício Prático: Compreendendo o Asyncio
import datetime
import asyncio


async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde a geração de {quantidade} dados')
    for i in range(quantidade):
        item = i * i
        await dados.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.01)
    print('Fim da geração de dados')


async def processar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde o processamento de {quantidade} dados')
    processados = 0
    while processados < quantidade:
        await dados.get()
        processados += 1
        await asyncio.sleep(0.01)
    print('Fim do processamento de dados')

if __name__ == '__main__':
    total = 5_000
    dados = asyncio.Queue()
    el = asyncio.get_event_loop()
    print(f'Computando {total*2:.2f} dados')
    el.run_until_complete(gerar_dados(total, dados))
    el.run_until_complete(gerar_dados(total, dados))
    el.run_until_complete(processar_dados(total*2, dados))
    el.close()
