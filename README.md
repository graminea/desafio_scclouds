# Desafio SCClouds

Resolução do desafio técnico proposto pela SCClouds, implementado em Python.
Duas implementações (recursiva e iterativa) para Fibonacci e Números Primos, com validação de entrada e testes.

## Como Executar

### Pré-requisitos

- Python 3.8+

### Rodar as funções

```bash
python -c "from fibo_recur import fibo_recur; print(fibo_recur(10))"
python -c "from primes_till_n_linear import primes_till_n_linear; print(primes_till_n_linear(30))"
```

### Rodar os testes

```bash
python testes_fibo.py
python testes_primes.py
```

## Estrutura do Projeto

```
├── fibo_recur.py               # Fibonacci recursivo
├── fibo_linear.py              # Fibonacci linear
├── primes_till_n_recur.py      # Primos recursivo
├── primes_till_n_linear.py     # Primos linear
├── testes_fibo.py              # Testes de Fibonacci (valor + validação)
├── testes_primes.py            # Testes de Primos (valor + validação)
```