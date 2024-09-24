'''Problem: Write a function first_non_repeating(lst) that finds the first element in a list that does not repeat. Use the in keyword to check if an element repeats.'''
def first_non_repeating(lst):
    new_lst =[]
    for item in lst:
        if item not in lst:
            new_lst.append(item)
        else:
            return item

x = first_non_repeating([4,5,6,4,5,7])
print(x)