row_col = int(input())
matrix = []
counter = 1
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(counter)
        counter += 1
print(*matrix, sep="\n")

total_sum = 0
for r in range(row_col):
    for c in range(r + 1):
        total_sum += matrix[r][c]
print(total_sum)