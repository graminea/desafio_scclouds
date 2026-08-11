from fibo_recur import fibo_recur
from fibo_linear import fibo_linear


CASOS_VALOR = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (20, 6765),
]

CASOS_VALIDACAO = [
    (-1, ValueError),
    (-10, ValueError),
    (3.5, TypeError),
    (0.0, TypeError),
    ("abc", TypeError),
    (None, TypeError),
    ([1, 2], TypeError),
]


def testar_valores(nome, funcao, casos):
    print(f"=== {nome} - Testes de valor ===\n")
    passou = 0
    falhou = 0
    for entrada, esperado in casos:
        resultado = funcao(entrada)
        if resultado == esperado:
            print(f"  [PASS] fib({entrada}) = {resultado}")
            passou += 1
        else:
            print(f"  [FAIL] fib({entrada}) = {resultado}  (esperado {esperado})")
            falhou += 1
    print(f"\n  Resultado: {passou} passou, {falhou} falhou\n")


def testar_validacao(nome, funcao, casos):
    print(f"=== {nome} - Testes de validação ===\n")
    passou = 0
    falhou = 0
    for entrada, erro_esperado in casos:
        try:
            funcao(entrada)
            print(f"  [FAIL] fib({entrada!r}) nao levantou excecao  (esperado {erro_esperado.__name__})")
            falhou += 1
        except Exception as e:
            if type(e) is erro_esperado:
                print(f"  [PASS] fib({entrada!r}) -> {type(e).__name__}: {e}")
                passou += 1
            else:
                print(f"  [FAIL] fib({entrada!r}) -> {type(e).__name__}  (esperado {erro_esperado.__name__})")
                falhou += 1
    print(f"\n  Resultado: {passou} passou, {falhou} falhou\n")


if __name__ == "__main__":
    testar_valores("Fibonacci Recursivo", fibo_recur, CASOS_VALOR)
    testar_valores("Fibonacci Linear", fibo_linear, CASOS_VALOR)

