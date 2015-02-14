"""
Objective: Print all the paths from left top corner to right bottom corner in two dimensional array.
Input: Two Dimensional array
Output: Print all the paths.
"""
def paths(matrix, row, column, path):

    if row == len(matrix)-1:
        for j in range(column, len(matrix)):
            path += str(matrix[row][j])
        print(path)
        return

    if column == len(matrix)-1:
        for i in range(row, len(matrix)):
            path += str(matrix[i][column])
        print(path)
        return

    path += str(matrix[row][column])

    paths(matrix, row+1, column, path)
    paths(matrix, row, column+1, path)
    # paths(matrix, row+1,column+1,path) # for diagonal paths

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

paths(M, 0, 0, "")
