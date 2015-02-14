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
from functools import reduce

def multiply(array):

    products = []

    for i in range(0, len(array)):
        previous = reduce(mul, array[:i]) if i else 1

        products.append(reduce(mul, array[i+1:], previous))

    return products

print(multiply([1, 7, 3, 4]))
