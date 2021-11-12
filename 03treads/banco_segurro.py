# Exemplo de concorrencia de Theads sem utilizar processos, aonde 2 threads vai tentar acessar o mesmo valor do banco
# mas agora sem dar erro pois estamos utilizando o with lock: 
import threading
import random
import time
from typing import List

lock = threading.RLock()

# construtor da conta


class Conta:
    def __init__(self, saldo=0) -> None:
        self.saldo = saldo


# iniciar o programa
def main():
    contas = criar_contas()
    with lock:
        # Somar o saldo de cada conta da lista de contas
        total = sum(conta.saldo for conta in contas)
    print('Iniciando Transferencias....')
    tarefas = [
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total))
    ]
    # Executar todas as threads criadas no tarefas
    [tarefa.start() for tarefa in tarefas]
    [tarefa.join() for tarefa in tarefas]
    print('Transferencias completas.')
    valida_banco(contas, total)


def servicos(contas, total):
    # Criar 10.000 contas
    for _ in range(1, 10_000):
        c1, c2 = pega_duas_contas(contas)
        # Valor entre 1 e 100 para fazer a transferencia
        valor = random.randint(1, 100)
        transferir(c1, c2, valor)
        valida_banco(contas, total)

# Após a -> é o retorno da função


def criar_contas() -> List[Conta]:
    # Criar uma lista de contas com um saldo entre 5k e 10k
    return[
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000))
    ]

# Para definir os tipos é nome do parmaetro : tipo do parametro


def transferir(origem: Conta, destino: Conta, valor: int):
    if origem.saldo < valor:
        return
    with lock:
        origem.saldo -= valor
        time.sleep(0.001)
        destino.saldo += valor

# Essa função recebe uma lista de contas e um total que vem da def main é o somatório


def valida_banco(contas: List[Conta], total: int):
    with lock:
        # Soma o saldo de todas as contas e se o total foi diferente do que tinha no começo ta errado.
        atual = sum(conta.saldo for conta in contas)
    if atual != total:
        print(
            f'Erro: Balanço bancario inconsisten. BRL {atual:.2f} vs {total:.2f}', flush=True)
    else:
        print(
            f'Tudo certo balanço consistente. BRL {atual:.2f} vs {total:.2f}', flush=True)

# Pega 2 contas aleatórias e retorna elas.


def pega_duas_contas(contas):
    c1 = random.choice(contas)
    c2 = random.choice(contas)
    while c1 == c2:
        c2 = random.choice(contas)
    return c1, c2


if __name__ == '__main__':
    main()
