"""
You have an array of integers, and for each index you want to find the product of every integer except the integer at that index.
For example, given:
  [1, 7, 3, 4]

your function would return:
  [84, 12, 28, 21]

by calculating:
  [7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.
"""
from operator import mul

def multiply(array):

    products = []
    previous = 1

    for i in range(0, len(array)):
        if i: previous = reduce(mul, array[:i])

        products.append(reduce(mul, array[i+1:], previous))

    return products

print multiply([1, 7, 3, 4])
