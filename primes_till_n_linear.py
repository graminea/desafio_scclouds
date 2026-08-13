
def is_prime(n):

    # teoricamente nunca receberá valores menores que 1, porém valido para garantir
    if n <= 1:
        return False
    # teoria que os divisores vem em par, então é apenas necessario checar até a raiz quadrada de n, não até n
    for i in range(2, int(n**0.5) + 1): # eleva nˆ0,5 para fazer a raiz de n
        if n % i == 0:
            return False
            
    return True

def primes_till_n_linear(n):

    if n <= 1:
        return "'n' deve ser maior que 1"
    return_list= []

    for i in range(2, n+1):
        if is_prime(i):
            return_list.append(i)

    return return_list  