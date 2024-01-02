row_cow = input("Input the numbers!").split(",")
matrix = []
row = int(row_cow[0])
cow = int(row_cow[1])
counter = 0
for i in range(row):
    matrix.append(input().split())
print(matrix)
for y in range(row-1):
    for x in range(cow-1):
        current_element = matrix[y][x]
        down_element = matrix[y+1][x]
        side_element = matrix[y][x+1]
        diagonal_element = matrix[y+1][x+1]

        if current_element == down_element == side_element == diagonal_element:
            counter += 1


print(counter)