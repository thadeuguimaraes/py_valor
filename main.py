def is_fibonacci(number):
    """
    Verifica se o número dado pertence à sequência de Fibonacci.
    """
    if number < 0:
        return False
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number

def fibonacci_sequence(limit):
    """
    Gera a sequência de Fibonacci até o limite dado.
    """
    sequence = [0, 1]
    while sequence[-1] < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Exemplo de uso
number = int(input("Digite um número: "))
sequence = fibonacci_sequence(number)
if number in sequence:
    print(f"{number} pertence à sequência de Fibonacci.")
else:
    print(f"{number} não pertence à sequência de Fibonacci.")
