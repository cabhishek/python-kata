""" Subsets possible from a list
"""
#def power_set(numbers):
    #sets = [[]]

    #if not numbers: return sets

    #sets += [numbers]

    #for i, number in enumerate(numbers):
        #sets.append([number])

        #for x in numbers[i+1:]:
            #sets.append([number] + [x])

    #return sets

def powerset(lst):
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

print powerset([1,2,3,4])

