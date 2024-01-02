rows, cols = list(map(int, input().split(", ")))

matrix = []

for _ in range(rows):
    matrix.append(input().split())

print(*matrix, sep="\n")
counter = 0

for r in range(rows - 1):
    for c in range(cols - 1):
        current_element = matrix[r][c]
        right_element = matrix[r][c + 1]
        down_element = matrix[r + 1][c]
        down_right_element = matrix[r + 1][c + 1]
        if current_element == right_element and down_element and down_right_element:
            counter += 1
print(counter)