
def flatten(arr, results=[]):

    for i in range(len(arr)):

        if isinstance(arr[i], list):
            results = flatten(arr[i], results)
        else:
            results += [arr[i]]
    else:
        return results

arr = [1, [2,3], [[4]], [[[[[5]]]]]]

# arr = [1,2,3,4,5]

print flatten(arr)
