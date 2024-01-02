num = int(input())
matrix = []

for _ in range(num):
    nums = list(map(int ,input().split()))
    matrix.append(nums)
primary_diagonal = 0
secondary_diagonal = 0
for i in range(num):
    primary_diagonal += matrix[i][i]
for i in range(num):
    secondary_diagonal += matrix[i][num - i - 1]

print(primary_diagonal)
print(secondary_diagonal)