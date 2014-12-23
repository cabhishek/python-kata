"""
Write a program to sort a stack in ascending order (with biggest item on top). You may use additional stacks to hold items, but you may not copy  the elements into
any other data structure (like array). The stack support the following operations push, pop, peek and is_empty.

"""


def sort_stack(stack):

    def peek(stack):
        return stack[-1:][0]

    sorted_stack = []

    while stack:
        number = stack.pop()

        if stack and number > peek(stack):
            sorted_stack.append(number)
        else:
            while sorted_stack and peek(sorted_stack) > number:
                stack.append(sorted_stack.pop())

            sorted_stack.append(number)

    return sorted_stack


print sort_stack([7, 73, 65, 23, 8])
