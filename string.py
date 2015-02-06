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

def reverse_vowels(string, vowels):
    start = 0
    end  = len(string) - 1
    string = list(string)

    while end > start:
        if string[start] in vowels and string[end] in vowels:
            string[start],string[end] = string[end], string[start]
            start += 1
            end  -= 1

        if string[start] not in vowels:
            start += 1

        if string[end] not in vowels:
            end -= 1

    return "".join(string)

print reverse("Hello World")
print reverse_2("Hello from Mars")
print reverse_3("Hello world everyone")

vowels = ["a", "e", "i", "o", "u"]
print reverse_vowels("abhishek", vowels)


def compress(string):

    if not string: return None

    # initialize
    compressed = string[0]
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            # append count
            compressed += str(count)
            # append next char
            compressed += string[i]
            # reset count
            count = 1
    else:
        # last char count value
        compressed += str(count)

    return min(compressed, string, key=len)

# string = "aabbbccc"
# string = "abb"
string = "abccccccccccccccccccccccccccccccdefg"

print compress(string)
