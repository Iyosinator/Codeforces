test_cases = int(input())
for _ in range(test_cases):
    matrix_size = int(input())
    diagonal_values = [0] * (2 * matrix_size + 1)
    is_value_used = [0] * (2 * matrix_size + 1)

    for row_index in range(1, matrix_size + 1):
        row_elements = list(map(int, input().split()))
        for col_index in range(1, matrix_size + 1):
            current_value = row_elements[col_index - 1]
            diagonal_sum = row_index + col_index
            if diagonal_values[diagonal_sum] == 0:
                diagonal_values[diagonal_sum] = current_value
                is_value_used[current_value] = 1

    for value in range(1, 2 * matrix_size + 1):
        if is_value_used[value] == 0:
            print(value, end=' ')
            break

    for i in range(2, 2 * matrix_size + 1):
        print(diagonal_values[i], end=' ')
    print()
