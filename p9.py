'''9.Write a function count_frequencies(lst): that takes a list as input and returns a dictionary where the keys are the elements of the list and the values are their frequencies.'''

def count_frequencies(lst):
    new_map = {}
    for item in lst:
        if item in new_map:
            new_map[item] += 1
        else:
            new_map[item] = 1
        
    return new_map

print(count_frequencies([1,1,1,2,3,4,5,6,7]))
    