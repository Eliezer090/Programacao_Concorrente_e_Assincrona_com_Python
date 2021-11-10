import threading
import time


def main():
    # Declara a thead o que vai ser executado e seus parametros
    threads = [
        threading.Thread(target=contador, args=('elefante', 10)),
        threading.Thread(target=contador, args=('buraco', 8)),
        threading.Thread(target=contador, args=('moeda', 23)),
        threading.Thread(target=contador, args=('pato', 12)),
    ]
    print('ANTES')
    # leva a thead criada anteriormente para uma piscina de theads que o sistema vai executar conforme disponibilidade
    # Percorre a lista threads e da o start Listcompreenshion, poderia ser feito com for normal
    [th.start() for th in threads]
    print('Após o start')
    # Quando demos o join dizemos que nao queremos sair daqui até que a thead nao acaba de processar
    [th.join() for th in threads]
    print('Após o join aqui acabou')


def contador(o_que, contador):
    for n in range(1, contador+1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
