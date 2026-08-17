def is_prime(n):
    """Verifica se um número é primo.

    Usa verificação até a raiz quadrada de n, pois divisores sempre vêm em pares 
    
    """

    # teoricamente nunca receberá valores menores que 1, porém valido para garantir
    if n <= 1:
        return False
    # teoria que os divisores vem em par, então é apenas necessario checar até a raiz quadrada de n, não até n
    for i in range(2, int(n**0.5) + 1): # eleva nˆ0,5 para fazer a raiz de n
        if n % i == 0:
            return False
            
    return True

def primes_till_n_linear(n):
    """Retorna todos os números primos até n usando iteração.

    """

    if type(n) is not int:
        raise TypeError(f"Input tem que ser um inteiro, recebeu um {type(n).__name__}")
    if n <= 1:
        raise ValueError(f"n tem que ser > 1, {n} não é > 1")

    primes = []

    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)

    return primes