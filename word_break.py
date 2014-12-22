"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

def word_break(word, dict):

    for i in range(len(word)):
        first  = word[:i]
        second = word[i:]

        if first in dict and second in dict:
            return True

    return False

print word_break("leetcode", ["leet", "code"])
