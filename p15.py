''''Check if a String is a Palindrome
Question: A palindrome is a word that reads the same backward as forward. Write a function to check if a string is a palindrome.'''
def is_palindrome(s):
    new_string=''
    for i in range(len(s)-1,-1,-1):
        new_string = new_string+s[i]
    
    if (new_string==s):
        return True

print(is_palindrome('sai'))