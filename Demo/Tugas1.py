from functools import reduce

def arithmetic_geometric_sequence(a, d, r, n) -> list:
    def recursive_term(k: int) -> float:
        if k == 1:
            return a
        return (a + (k - 1) * d) * r**(k - 1)
    
    return [recursive_term(i) for i in range(1, n + 1)]

def add(x, y):
    return x + y

def calculate_sum(sequence: list):
    return reduce(add, sequence)


a, d, r, n = 2, 3, 2, 5
sequence = arithmetic_geometric_sequence(a, d, r, n)
sequence_sum = calculate_sum(sequence)
    
print(f"Sequence: {sequence}")
print(f"Sum: {sequence_sum}")    
