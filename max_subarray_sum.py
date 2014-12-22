"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4], the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""

def max_subarray_sum(array):
    if not array: return 0

    max_sum = array[0]
    sum_so_far = array[0]

    for number in array[1:]:
        sum_so_far = max(sum_so_far+number, number)
        max_sum = max(max_sum, sum_so_far)

    return max_sum

print max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])
