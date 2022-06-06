import asyncio
import aiofiles
import aiohttp
import bs4
import datetime


async def pegar_links():
    links = []
    async with aiofiles.open('05_Programacao_Assincrona/links.txt') as arq:
        async for linha in arq:
            links.append(linha.strip())
    return links


async def pegar_html(link):
    print(f'Pegando o html do link: {link}')
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            resp.raise_for_status()
            return await resp.text()


def get_titulo(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    return soup.title.string.split('|')[0].strip()


'''
# Duas formas de fazer a mesma coisa só esta é mais lenta
async def imprimir_titulos():
    inicio = datetime.datetime.now()
    links = await pegar_links()
    for link in links:
        html = await pegar_html(link)
        titulo = get_titulo(html)
        print(f'Título: {titulo}')
    fim = datetime.datetime.now()
    result = fim - inicio
    print(f'Acabou execução em: {result}')
'''


# Forma mais rapida de busca
async def imprimir_titulos():
    inicio = datetime.datetime.now()
    links = await pegar_links()
    tarefas = []
    for link in links:
        tarefas.append(asyncio.create_task(pegar_html(link)))

    for tarefa in tarefas:
        html = await tarefa
        titulo = get_titulo(html)
        print(f'Título: {titulo}')

    fim = datetime.datetime.now()
    result = fim - inicio
    print(f'Acabou execução em: {result}')


def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(imprimir_titulos())
    el.close()


if __name__ == '__main__':
    main()
