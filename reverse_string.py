def reverse(string):
    if not string: return ""

    return " ".join(string.split()[::-1])


def reverse_2(string):
    if not string: return ""

    array = string.split()
    start = 0
    end   = len(array) - 1

    while end > start:
        array[start], array[end] = array[end], array[start]

        start += 1
        end -= 1

    return " ".join(array)

print reverse("Hello World")
print reverse_2("Hello from Mars")
