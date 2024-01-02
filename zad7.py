row_col = int(input())
matrix = []
for row in range(row_col):
    current_row = list(input()) #list(map(str, input()))
    matrix.append(current_row)
searched_element = input()

# element_is_find = False
for r in range(row_col):
    for c in range(row_col):
        current_element = matrix[r][c]
        if current_element == searched_element:
            print(f"({r}, {c})")
            # element_is_find = True
            break
        break

else:
    print("element not find")