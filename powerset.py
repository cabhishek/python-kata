""" Subsets possible from a list
"""
def power_set(numbers):
    if not numbers: return [[]]

    sets = [[]]
    sets += [numbers]

    for i, number in enumerate(numbers):
        sets.append([number])

        for x in numbers[i+1:]:
            sets.append([number] + [x])

    return sets

print power_set([1,2,3])
