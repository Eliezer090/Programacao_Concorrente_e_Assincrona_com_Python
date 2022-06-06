# 35. Exercício Prático: Eventos Multitarefas com Loop de Eventos e Corrotinas
import asyncio
import datetime


async def diz_oi_demorado():
    print('Oi')
    await asyncio.sleep(5)
    print('todos')


el = asyncio.get_event_loop()
el.run_until_complete(diz_oi_demorado())
el.close()

