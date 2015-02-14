def insert_sort(A):

    for i in range(1, len(A)):
        j = i

        while j-1 >= 0:

            if A[j] < A[j-1]:
                # swap
                A[j-1], A[j] = A[j], A[j-1]

            j -= 1

    return A

# A = [4,5,3,19,2,20,1,8]
# A = [4,5,3,19,2,20]
A = [9,8,7,6,5,4,3,2,1]

print(insert_sort(A))

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot  = arr[len(arr) / 2]

    left   = [x for x in arr if x < pivot ]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot ]

    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))
