'''7. Count Occurrences of Element
Problem: Write a function count_occurrences(lst, item) that returns the number of times an element appears in the list.'''

def count_occurrences(lst, item):
    count =0
    for element in lst:
        if item == element:
            count += 1
    return count
        
            
        

print(count_occurrences([1,1,1,2,3,4,5], 1))