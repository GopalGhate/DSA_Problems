"""
Find if 2 strings are anagrams of each other or not
Solution - Use ascii value and create an maintain an array of 26 chars.
TC - O(m+n), where m and n is the length of given string
SC - O(1)
"""

def is_anagram(a, b):
    s1 = [0 for i in range(26)]
    s2 = [0 for i in range(26)]

    for i in range(len(a)):
        index = ord(a[i]) - ord('a')
        s1[index] += 1

    for i in range(len(b)):
        index = ord(b[i]) - ord('a')
        s2[index] += 1
    return s1 == s2

print(is_anagram("abc", "cba"))
print(is_anagram("abc", "dbac"))