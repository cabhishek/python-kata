def loop(array):

    print('Basic')
    for number in array:
        print(number)

    print('Basic + Loop index')
    for i, number in enumerate(array):
        print(i, number)

    print('Start from index 1')
    for i in range(1, len(array)):
        print(array[i])

    print('Choose index and start position')
    for i, number in enumerate(array[1:], start=1):
        print(i, number)

    print('Basic while loop')
    i = 0
    while i < len(array):
        print(i, array[i])
        i +=1

    print('Simulate \'while\' with \'for\'')
    for i in range(len(array)):
        print(i, array[i])

    print('Basic backward loop')
    for number in array[::-1]:
        print(number)

    print('Backward loop with index')
    for i in range(len(array)-1, -1,-1):
        print(array[i])

    print('Loops with flexible step number')
    for number in array[::2]:
        print(number)

    print('Iterate Curr and next element')
    for (curr, next) in zip(array, array[1:]):
        print(curr, next)

loop([1,2,3,4,5,6,7,8,9,10])
