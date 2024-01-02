# N = int(input())
# matrix = []
# for _ in range(N):
#     row = list(map(int, input().split(", ")))
#     matrix.append(row)
#
# secondary_diagonal_sum = sum(matrix[i][N - 1 - i] for i in range(N))
#
# print(secondary_diagonal_sum)

row_col = int(input())
matrix = []
counter = 1
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(counter)
        counter += 1
print(*matrix, sep="\n")

secondary_diagonal_sum = 0
for r in range(row_col):
    secondary_diagonal_sum += matrix[r][row_col - 1 - r]
