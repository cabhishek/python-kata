def reverse(array):

    def rec_reverse(array, low, high):

        if low > high: return array
        # swap
        array[low], array[high] = array[high], array[low]

        return rec_reverse(array, low+1, high-1)

    return rec_reverse(array, 0, len(array)-1)

print reverse([4,5,6,3,9])
