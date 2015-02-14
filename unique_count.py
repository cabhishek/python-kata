def unqiue_count(array):

    if not array: return 0

    count = 1

    for i in range(len(array)-1):
        if array[i] != array[i+1]:
            count += 1

    return count

print(unqiue_count([1,2,3,4,5,6,6,7]))
