'''Invert a dictionary
Write a function to invert a dictionary, i.e., make the values the keys and the keys the values. Assume that the values in the dictionary are unique.'''
def invert_dict(d):
    new_d = {}
    for k,v in d.items():
        new_d[v]=k
    return new_d

print(invert_dict({'a': 1, 'b': 2, 'c': 3}))
