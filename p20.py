'''7. Longest Substring Without Repeating Characters
Question:
Given a string, find the length of the longest substring without repeating characters.

Example:
Input: "abcabcbb"
Output: 3 ("abc")'''

def length_of_longest_substring(s):
    new_map = {}
    lst = []
    key=''
    max=0
    for char in s:
        if char not in lst:
            lst.append(char)
        else:
            key = ''.join(lst)
            new_map[key]=len(key)
            lst.clear()
            lst.append(char)

    for k,v in new_map.items():
        if v > max:
            max = v

    for key,val in new_map.items():
        if val == max:
            return key,val       

        
    
    

print(length_of_longest_substring("basedonabcabcdbb"))