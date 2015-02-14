"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
Please dont use built in min function.
"""
def min_path_sum(triangle):
    min_sum = 0

    for row in triangle:
        row_min = row [0]

        for i in range(1, len(row)):
            if row[i] < row_min:
                row_min = row[i]

        min_sum += row_min

    return min_sum

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(min_path_sum(triangle))
