mat = []
n = int(input())

for i in range(n):
    mat.append(list(map(int, input().split())))

diag_sum = 0
diag_sum_other = 0
for i in range(n):
    diag_sum_other += mat[i][i]
    diag_sum += mat[i][n-i - 1]
print(diag_sum)
print(diag_sum_other)