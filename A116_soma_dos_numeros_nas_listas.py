import itertools

numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_2 = [1, 2, 3, 4, 5, 6]
sum_lists = []

interval = min(len(numbers_1), len(numbers_2))

for i in range(interval):
    sum_lists.append((numbers_1[i] + numbers_2[i]))

print(sum_lists)

sum_lists = [x + y for x, y in zip(numbers_1, numbers_2)]  # mesma coisa

print(sum_lists)

sum_lists = [x + y for x, y in itertools.zip_longest(numbers_1, numbers_2, fillvalue=0)]  # fillvalue explicitamente sendo 0 para não gerar erro de soma com None

print(sum_lists)
