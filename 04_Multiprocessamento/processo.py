'''Multi Processos '''
import multiprocess as mp
print(f'Iniciando o processo com nome: {mp.current_process().name}')


def funcao(valor):
    print(f'Fazendo algo com o {valor}')


def main():
    pc = mp.Process(target=funcao, args=('Passaro',), name='Processo Geek')
    print(f'Iniciando: {pc.name}')
    pc.start()
    pc.join()


if __name__ == '__main__':
    main()
