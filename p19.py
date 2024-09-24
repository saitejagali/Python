'''String Compression
Question: Implement basic string compression using the counts of repeated characters. If the "compressed" string is not smaller than the original, return the original string.
Example:
Input: "aabcccccaaa"
Output: "a2b1c5a3"'''
def compress_string(s):
    lst = []
    count =1
    for char in range(1,len(s)):
        if s[char]==s[char-1]:  #present charachter s[char] is equal to previus character s[char-1] icrement the count value
            count += 1
        else:
            lst.append(s[char-1]+str(count))
            count=1
    
    lst.append(s[-1]+str(count))
    new_string = ''.join(lst)
    return new_string


print(compress_string("aabcccccaaa"))


