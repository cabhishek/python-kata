def matrix_search(number, matrix):
    row = 0
    column = len(matrix)-1

    while row < len(matrix) and column >= 0:
        if matrix[row][column] == number: return True

        if number > matrix[row][column]:
            row +=1
        else:
            column -= 1

    return False

matrix = [
            [10, 20, 30, 40],
            [15, 25, 35, 45],
            [27, 29, 37, 48],
            [32, 33, 39, 50],
        ];

print(matrix_search(37, matrix))
