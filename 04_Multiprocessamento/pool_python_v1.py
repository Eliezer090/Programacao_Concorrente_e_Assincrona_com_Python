import multiprocess as mp


def calcular(dado):
    return dado ** 2


def main():
    tamanho_pool = mp.cpu_count()*2
    print(f'Tamanho da pool {tamanho_pool}')
    # Criando uma pool ou uma piscina de processos
    pool = mp.Pool(processes=tamanho_pool)
    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)
    print(f'Saidas: {saidas}')
    # Close serve para dizer que pode fechar o pool e pode executar
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
