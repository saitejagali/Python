'''5. Anagram Check
Question: Check if two strings are anagrams of each other.
Example:
Input: "listen", "silent"
Output: True
'''
def are_anagrams(s1, s2):
    return sorted(s1)==sorted(s2)
        
print(are_anagrams('lsiten','silent'))