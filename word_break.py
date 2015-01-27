"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

def word_break_2(word, dict):

    for i in range(len(word)):
        first  = word[:i]
        second = word[i:]

        if first in dict and second in dict:
            return True

    return False

print word_break_2("leetcode", ["leet", "code"])


dict = ["leet", "code", "is", "great", "mark", "for"]
string = "leetcodeismark"

# More general case.
def word_break(string, dict):
    words = []

    def find_words(string):
        for i in range(len(string)+1):
            prefix = string[:i]

            if prefix in dict:
                words.append(prefix)
                find_words(string[i:])

    find_words(string)

    return " ".join(words)

print word_break(string, dict)

# without closure
def word_break_3(string, dict):

    if string in dict: return [string]

    for i in range(len(string)+1):
        prefix = string[:i]

        if prefix in dict:
            return [prefix] + word_break_3(string[i:], dict)

    return []

print " ".join(word_break_3(string, dict))
