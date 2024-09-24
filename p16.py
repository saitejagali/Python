'''P17. Count Vowels and Consonants
Question: Write a function that counts the number of vowels and consonants in a string'''

#usage of string methods like isalpha,isalnum,isdecimal,ispace,istitle

def count_vowels_consonants(s):
    vowels='aeiouAEIOU'
    v_count,c_count = 0,0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count,c_count

print(count_vowels_consonants('saiteja'))
