# Codigo anterior sem nenhuma modificação
"""
import math


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    final = 0
    while pos < fim:
        pos += 1
        final = math.sqrt((pos-fator)*(pos-fator))
    print(final)
"""


# Codigo modificado para Cython
import cython
from libc.math cimport sqrt


def computar(fim: cython.double, inicio: cython.double = 1):
    pos: cython.double = inicio
    fator: cython.double = 1000 * 1000
    final: cython.double = 0
    # nogil para dizer para o Cython ignorar o python e converter para C TUDO
    with nogil:
        while pos < fim:
            pos += 1
            final = sqrt((pos-fator)*(pos-fator))

    return final
