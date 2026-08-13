from primes_till_n_recur import primes_till_n_recur
from primes_till_n_linear import primes_till_n_linear


CASOS_VALOR = [
    (2, [2]),
    (3, [2, 3]),
    (4, [2, 3]),
    (5, [2, 3, 5]),
    (10, [2, 3, 5, 7]),
    (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
]

CASOS_VALIDACAO = [
    (1, ValueError),
    (0, ValueError),
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
        try:
            resultado = funcao(entrada)
        except Exception as e:
            print(f"  [FAIL] primes({entrada}) levantou {type(e).__name__}: {e}  (esperado {esperado})")
            falhou += 1
            continue

        if resultado == esperado:
            print(f"  [PASS] primes({entrada}) = {resultado}")
            passou += 1
        else:
            print(f"  [FAIL] primes({entrada}) = {resultado}  (esperado {esperado})")
            falhou += 1
    print(f"\n  Resultado: {passou} passou, {falhou} falhou\n")
    return passou, falhou


def testar_validacao(nome, funcao, casos):
    print(f"=== {nome} - Testes de validação ===\n")
    passou = 0
    falhou = 0
    for entrada, erro_esperado in casos:
        try:
            funcao(entrada)
            print(f"  [FAIL] primes({entrada!r}) nao levantou excecao  (esperado {erro_esperado.__name__})")
            falhou += 1
        except Exception as e:
            if type(e) is erro_esperado:
                print(f"  [PASS] primes({entrada!r}) -> {type(e).__name__}: {e}")
                passou += 1
            else:
                print(f"  [FAIL] primes({entrada!r}) -> {type(e).__name__}  (esperado {erro_esperado.__name__})")
                falhou += 1
    print(f"\n  Resultado: {passou} passou, {falhou} falhou\n")
    return passou, falhou


if __name__ == "__main__":
    resultados = []
    resultados.append(testar_valores("Primes Recursivo", primes_till_n_recur, CASOS_VALOR))
    resultados.append(testar_valores("Primes Linear", primes_till_n_linear, CASOS_VALOR))
    resultados.append(testar_validacao("Primes Recursivo", primes_till_n_recur, CASOS_VALIDACAO))
    resultados.append(testar_validacao("Primes Linear", primes_till_n_linear, CASOS_VALIDACAO))

    total_passou = sum(p for p, f in resultados)
    total_falhou = sum(f for p, f in resultados)
    print(f"=== TOTAL GERAL: {total_passou} passou, {total_falhou} falhou ===")

    if total_falhou > 0:
        exit(1)
