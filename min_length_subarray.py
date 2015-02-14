"""
Given an array and an integer, find the smallest subarray whose sum is greater than the given integer.
"""
def min_length_subarray(A, x):

    start, end = 0, 0
    min_length = len(A)
    curr_sum = 0

    for i in range(len(A)):

        curr_sum += A[i]

        while curr_sum > x:

            #After subtract if sum is still greater
            #and min length condition is still met
            if curr_sum - A[start] > x and \
                    (i-start) < min_length:

                curr_sum -= A[start]

                #new limits
                min_length = (i - start) + 1
                start += 1
                end = i
            else:
                break

    return A[start:end+1]

# A = [1, 5, 20, 70, 8]  #97
A = [1, 10, 3, 40, 18]  # 50

# A = [1, 4, 45, 6, 0, 19] #51

print(min_length_subarray(A, 50))
