'''Problem: Write a function is_sublist(lst1, lst2) that checks if lst1 is a sublist of lst2. Use the in keyword to check if elements of lst1 are in lst2.'''

def is_sublist(lst1, lst2):
    new_lst=[]
    for item in lst1:
        if item in lst2:
            new_lst.append(item)
    return new_lst

x= is_sublist(['s','t','g'],['s','t'])
print(x)
            