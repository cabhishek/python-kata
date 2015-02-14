def delete_from_array(number, array):
    swap_idx = 0

    for i in range(len(array)):
        if number == array[i]:
            # Mark empty by setting 0
            array[i] = 0
            # If more than one match then move
            # all those matched elements along.
            # so go father back.
            swap_idx = min(i, swap_idx)
        else:
            # Swap
            array[swap_idx], array[i] = array[i], array[swap_idx]
            swap_idx += 1

    return array


print(delete_from_array(3, [5,3,7,11,2,3,13,5,7,3,9,8]))
