'''8. Sum of Unique Elements
Problem: Write a function sum_unique(lst) that returns the sum of all unique elements in the list (i.e., elements that appear only once).'''

def sum_unique(lst):
    sum = 0
    new_list = []
    for item in lst:
        if lst.count(item)==1:
            new_list.append(item)
    for i in new_list:
        sum += i
    return sum
        
print(sum_unique([1,2,2,3,4,4,5,6]))      