def double(x):
    return x * 2

#2. Data berupa sequence/iterable data
numbers = [1, 2, 3, 4, 5]

#3. Penggunaan fungsi map
doubled_numbers = set(map(double, numbers))
print(doubled_numbers)