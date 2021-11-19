'''COMUNICANDO dados entre processos com Pipe'''
import multiprocess as mp


def ping(conn):
    # Var realizar um Send da MSG
    conn.send('Geek')


def pong(conn):
    # recv é o metodo que recebe a msg
    msg = conn.recv()
    print(f'Mensagem: {msg}')


def main():
    # Pipe é para fazer uma ligação entre os processos, o true é se vai enviar e se vai receber
    # Com Pipe nao é possivel dar lock o melhor é Queue
    conn1, conn2 = mp.Pipe(True)

    p1 = mp.Process(target=ping, args=(conn1,))
    p2 = mp.Process(target=pong, args=(conn2,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
