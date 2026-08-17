def fibo_linear(N):
    
    if type(N) is not int:
        raise TypeError(f"Input tem que ser um inteiro, recebeu um {type(N).__name__}")
    if N < 0:
        raise ValueError(f"N >= 0, {N} não é >= 0")
    
    if N <= 1:
        return N
    if N == 2:
        return 1

    anterior, atual = 0, 1
    for _ in range(2, N + 1):
        anterior, atual = atual, anterior + atual

    return atual
