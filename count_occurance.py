def binary_search(array, number, search_first):
    low = 0
    high = len(array) - 1
    result = 0

    while low <= high:

        mid = (low + high) / 2

        if array[mid] == number:
            result = mid

            if search_first:
                high = mid - 1
            else:
                low = mid + 1

        elif number > array[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return result

a = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11]

first = binary_search(a, 1, True)
last = binary_search(a, 1, False)

print (last - first) + 1 if first or last else 0
