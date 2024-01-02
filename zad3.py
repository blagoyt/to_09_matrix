m, n = [int(x) for x in input().split(", ")]
#m, n = map(int, input().split(", "))
mat = []

for i in range(m):
    mat.append(list(map(int, input().split())))

max_sum = float("-inf")
num_str = []

for y in range(m - 2):
    for x in range(n - 2):
        line_1 = mat[y][x:x+3]
        line_2 = mat[y+1][x:x+3]
        line_3 = mat[y+2][x:x+3]
        cur_sum = sum(line_1) + sum(line_2) + sum(line_3)

        if cur_sum > max_sum:
            max_sum = cur_sum
            num_str= [line_1, line_2, line_3]

print(max_sum)
print(num_str)