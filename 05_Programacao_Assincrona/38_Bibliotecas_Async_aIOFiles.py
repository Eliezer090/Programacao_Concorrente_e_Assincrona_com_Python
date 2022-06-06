import asyncio
import aiofiles


async def exemplo_arq1():
    async with aiofiles.open('05_Programacao_Assincrona/texto.txt') as arq:
        conteudo = await arq.read()
    print(conteudo)


async def exemplo_arq2():
    async with aiofiles.open('05_Programacao_Assincrona/texto.txt') as arq:
        async for linha in arq:
            print(linha)


def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(exemplo_arq2())
    el.close()


if __name__ == '__main__':
    main()
