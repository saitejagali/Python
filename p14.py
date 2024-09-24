'''1. Reverse a String
Question: Given a string, return the string in reverse order.'''

def reverse_string(s):
    new_string=''
    for i in range(len(s)-1,-1,-1):
        new_string = new_string+s[i]
    return new_string
    

print(reverse_string("sai"))