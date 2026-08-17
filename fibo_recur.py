def fibo_recur(N):
    
    if type(N) is not int:
        raise TypeError(f"Input tem que ser um inteiro, recebeu um {type(N).__name__}")
    if N < 0:
        raise ValueError(f"N >= 0, {N} não é >= 0")
    if N == 0:
        return 0
    if N == 1:
        return 1

    return fibo_recur(N - 1) + fibo_recur(N - 2)
