""" Subsets possible from a list
"""

def powerset_2(lst):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in lst:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [x] onto everything in the
        # previous power set)
        result.extend([subset + [x] for subset in result])
    return result

sets  = powerset_2(['a', 'b', 'c', 'd'])
print("Total sets ->", len(sets))
for set in sets:
    print(set)

def powerset(data):
    sets = [[]]
    idx = 1

    for x in data:
        new_sets = [[x]]

        for y in data[idx:]:
            # new set combinations
            new_sets += [set + [y] for set in new_sets]

        sets.extend(new_sets)

        idx += 1

    return sets

sets  = powerset(['a', 'b', 'c', 'd'])

print("Total sets ->", len(sets))

for set in sets:
    print(set)
