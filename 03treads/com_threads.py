# Processamento de 2 Theads aonde a segunda pendende dos dados da 1°
import time
import colorama
from threading import Thread
from queue import Queue


def gerador_de_dados(queue):
    for i in range(1, 11):
        # Flush é uma execução limpa nao espera nada.
        print(colorama.Fore.GREEN + f'Dados {i} gerado.', flush=True)
        time.sleep(1)
        queue.put(i)


def consumidor_de_dados(queue):
    # qsize obtem quantos objetos tem na lista
    while queue.qsize() > 0:
        # o get pega e remove o valor da lista
        valor = queue.get()
        print(colorama.Fore.RED + f'Dado {valor * 2} processado', flush=True)
        time.sleep(1)
        # task_done é para dizer que a tarefa está concluida
        queue.task_done()


if __name__ == '__main__':
    print('Sistema Iniciado', flush=True)
    # Cria uma Queue nova
    queue = Queue()
    # Cria as Threads
    th1 = Thread(target=gerador_de_dados, args=(queue,))
    th2 = Thread(target=consumidor_de_dados, args=(queue,))
    # Joga ela na picina
    th1.start()
    # Respera a execução para poder continuar
    th1.join()

    th2.start()
    th2.join()
