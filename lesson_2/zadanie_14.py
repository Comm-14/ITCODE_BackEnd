# Произвольный двумерный список
a = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [31, 32, 33, 34, 35],
    [51, 52, 53, 54, 55]
]
transposed = [[row[i] for row in a] for i in range(len(a[0]))]
for row in transposed:
    print(row)