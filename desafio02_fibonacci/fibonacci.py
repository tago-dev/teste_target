def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

numero = int(input('Digite um número: '))

print(f"O número {numero} {'pertence' if is_fibonacci(numero) else 'não pertence'} à sequência de Fibonacci")
