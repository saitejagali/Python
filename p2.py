'''Problem: Write a function remove_duplicates(lst) that removes all duplicate elements from a list. Use the in keyword to check for duplicates'''

def remove_duplicates(lst):
    new_list=[]
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

print (remove_duplicates([1,1,2,2,4,5]))