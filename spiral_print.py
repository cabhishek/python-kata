"""
Print 2-D array in spiral order
Commented code show traversing using while loop
"""

def spiral_traverse(matrix):

    if not len(matrix): return

    top = left = 0
    bottom = len(matrix)-1
    right = len(matrix[0]) -1

    dir = 0

    while top <= bottom:

        # go right
        if dir == 0:
            # i = left

            for i in range(left, right+1):
            # while i <= right:
                yield matrix[top][i]
                # i += 1
            top += 1

        # go down
        elif dir == 1:
            # j = top
            for j in range(top, bottom+1):

            # while j <= bottom:
                yield matrix[j][right]
                # j += 1

            right -= 1

        # go left
        elif dir == 2:
            # k = right

            for k in range(right, left-1, -1):
            # while k >= left:
                yield matrix[bottom][k]
                # k -= 1

            bottom -= 1

        # go up
        else:
            # p = bottom

            for p in range(bottom, top-1, -1):
            # while p >= top:
                yield matrix[p][left]
                # p -= 1

            left += 1

        # change direction
        dir = (dir + 1) % (len(matrix))

matrix = [[2,4,6,8],
          [5,9,12,16],
          [2,11,5,9],
          [3,2,1,8]]

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# matrix = [[1,2],
#           [4,5],
#           [7,8]]

# matrix = []

print([data for data in spiral_traverse(matrix)])
