import multiprocess as mp


def calcular(dado):
    return dado ** 2


def imprimirNomeProcesso():
    print(f'Iniciando o processo com o nome: {mp.current_process().name}')


def main():
    tamanho_pool = mp.cpu_count()*2
    print(f'Tamanho da pool {tamanho_pool}')
    # Criando uma pool ou uma piscina de processos, e para cada processo que for criado
    #  vai ser executad o initializer antes.
    pool = mp.Pool(processes=tamanho_pool, initializer=imprimirNomeProcesso)
    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)
    #saidas = pool.map(calcular, saidas)
    print(f'Saidas: {saidas}')
    # Close serve para dizer que pode fechar o pool e pode executar
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
