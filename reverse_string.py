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

def reverse_3(string):

    def reverse(string):
        start = 0
        end   = len(string)-1
        string = list(string)

        while end > start:
            string[start], string[end] = string[end], string[start]

            start += 1
            end   -= 1

        return "".join(string)

    string = list(reverse(string))
    i = 0
    reversed = ""

    for j in range(len(string)):
        if string[j] == ' ':

            if not reversed:
                reversed = reverse(string[i:j])
            else:
                reversed = reversed + " " + reverse(string[i:j])

            i = j + 1

    return reversed + " " +  reverse(string[i:])

print reverse("Hello World")
print reverse_2("Hello from Mars")
print reverse_3("Hello world everyone")
