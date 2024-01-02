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
list_elements = []
for r in range(row_col - 1):
    for c in range(row_col - 1):
        current_element = matrix[r][c]
        right_element = matrix[r][c + 1]
        down_element = matrix[r + 1][c]
        down_right_element = matrix[r + 1][c + 1]
        current_sum = current_element + right_element + down_element + down_right_element
        if total_sum < current_sum:
            total_sum = current_sum
            list_elements.clear()
            list_elements.extend([current_element, right_element, down_element, down_right_element])


for el in range(len(list_elements)):
    if el % 2 == 0:
        print(list_elements[el], end=" ")
    else:
        print(list_elements[el])
print(total_sum)