import threading
import time


def main():
    # Declara a thead o que vai ser executado e seus parametros
    th = threading.Thread(target=contador, args=('elefante', 10))
    print('ANTES')
    # leva a thead criada anteriormente para uma piscina de theads que o sistema vai executar conforme disponibilidade
    th.start()
    print('Após o start')
    # Quando demos o join dizemos que nao queremos sair daqui até que a thead nao acaba de processar
    th.join()
    print('Após o join aqui acabou')


def contador(o_que, contador):
    for n in range(1, contador+1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
