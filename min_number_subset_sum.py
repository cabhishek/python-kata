"""
Objective: Given a sorted array of positive integers, find out the smallest integer which cannot be represented as the sum of any subset of the array
Output: The smallest number which cannot be represented as the sum of any subset of the given array

Examples :

Array {1,1,3,4,6,7,9} smallest Number : 32

Array {1,1,1,1,1} smallest Number : 6

Array {2,3,6,7} smallest Number : 1

Array {1,2,6,7,9} smallest Number : 4

"""

def smallest_integer(array):
    smallest_int = 1

    for i in range(len(array)):
        if array[i] <= smallest_int:
            smallest_int += array[i]
        else:
            break

    return smallest_int

print smallest_integer([1,2,6,7,9])
