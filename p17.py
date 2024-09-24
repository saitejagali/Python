'''4. Find the First Non-Repeating Character
Question: Given a string, find the first non-repeating character.
Example:
Input: "swiss"
Output: "w"
'''
def first_non_repeating_char(s):
    new_map={}
    for char in s:
        if char  in new_map:
            new_map[char] += 1
        else:
            new_map[char] = 1
    
    for k,v in new_map.items():
        if (v==1):
            return k
        
print(first_non_repeating_char('swiss'))
