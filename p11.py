'''3. Merge two dictionaries
Write a function that takes two dictionaries as input and returns a new dictionary that combines them. If both dictionaries contain the same key, 
the value from the second dictionary should overwrite the value from the first dictionary.'''
def merge_dicts(dict1, dict2):
    new_dict = {}
    for k,v in dict1.items():
        new_dict[k]=v
    for k,v in dict2.items():
        new_dict[k]=v
    return new_dict

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))