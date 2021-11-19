'''COMUNICANDO DADOS entre processos com Queue'''

import multiprocess as mp


def ping(queue):
    # Vai realizar um Send da MSG
    queue.put('Geek')


def pong(queue):
    # get é o metodo que pega a msg
    msg = queue.get()
    print(f'Mensagem: {msg}')


def main():
    # Com o Queue pode ser feito o Lock se precisar
    queue = mp.Queue()

    p1 = mp.Process(target=ping, args=(queue,))
    p2 = mp.Process(target=pong, args=(queue,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
