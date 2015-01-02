"""
Given an array and an integer, find the smallest subarray whose sum is greater than the given integer.
"""
def min_length_subarray(array, x):

    start = 0
    ansEnd = 0
    ansStart = 0
    currSum = 0
    minLen = len(array)

    i = 0

    while True:
        while currSum > x:
            currSum = currSum - array[start]

            if i - start < minLen:
                minLen = i - start
                ansEnd = i
                ansStart = start

            start += 1

        if i < len(array):
            currSum += array[i]
        else:
            break

        i += 1

    return array[ansStart:ansEnd]

# A = [1, 5, 20, 70, 8]  #97
A = [1, 10, 3, 40, 18]  # 50

# A = [1, 4, 45, 6, 0, 19] #51

print min_length_subarray(A, 50)
