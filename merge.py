def merge(A, B):

    j = len(B) - 1
    i = len(A) - len(B) - 1
    free = len(A) - 1

    while j >= 0:

        if i >=0 and A[i] >= B[j]:
            A[free] = A[i]
            free -= 1
            i -= 1
        else:
            A[free] = B[j]
            free -= 1
            j -=1

    return A


A = [3,6,8,9,None,None,None]
B = [4,11,18]
# B = [15,16,17]
# B = [0,1,2]

print merge(A, B)

def arrange(A, k):
    # All elments less than A[K] before and greater after A[K]
    array = [None] * len(A)
    i = 0
    j = len(A)-1

    start = 0
    end = len(A)-1

    while i < k:

        if A[i] >= A[k]:
            array[end] = A[i]

            end -=1
            i +=1
        else:
            array[start] = A[i]
            start += 1
            i += 1

    while j > k:

        if A[j] <= A[k]:
            array[start] = A[j]
            start +=1
            j -=1
        else:
            array[end] = A[j]
            end -=1
            j -=1

    array[end] = A[k]

    return array



# A = [4,8,2,12,18,4,1]
A = [10,12,13,14,4,5,6,7]

print arrange(A,2)
