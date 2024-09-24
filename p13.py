'''5. Find common keys in two dictionaries
Write a function that returns a list of keys that are common between two dictionaries.'''

def common_keys(dict1, dict2):
    com_key={}
    for k,v in dict2.items():
        if k in dict1:
            com_key[k]=v
    return com_key

print(common_keys({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
        