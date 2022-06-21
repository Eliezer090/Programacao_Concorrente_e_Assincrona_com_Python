import datetime
import computa


def main():
    inicio = datetime.datetime.now()
    retorno = computa.computar(inicio=1, fim=50_000_000)
    fim = datetime.datetime.now()
    tempo = fim - inicio
    print(f'Terminou em {tempo.total_seconds():.2f} segundos!')
    print(retorno)


if __name__ == '__main__':
    main()


"""
Executando com computa.py:
    Terminou em 16.55 segundos!
Executando após buildado para C com Cyton:
    Terminou em 12.00 segundos!
Executando após converter para Cython o computa.pyx:
    Terminou em 10.00 segundos!
Executando com nogil(Ignora o python e transcreve tudo para C e tipando os campos):
    Terminou em 00.08 segundos!
"""
