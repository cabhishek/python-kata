def merge(A, B):

    j = len(B) - 1
    i = len(A) - len(B) - 1
    free = len(A) - 1

    while j >= 0:

        if i >=0 and A[i] >= B[j]:
            A[free] = A[i]
            A[i] = None # Mark empty
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
