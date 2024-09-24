''' Given a list of numbers from 1 to n with one number missing, write a function find_missing_number(lst, n) that returns the missing number using the in keyword.'''
def find_missing_number(lst, n):
    for i in range(1,n):
        if i not in lst:
            return i
        

x= find_missing_number([1,2,3,4,5,6,7,8,10],10)
print(x)