'''Given a dictionary with integer values, write a function to find the key with the maximum value'''
def max_value_key(d):
    new_map={}
    max_key=None
    max_value=0
    for k,v in d.items():
        if (v > max_value):
            max_value= v
            max_key = k
    new_map[max_key]=max_value
    return new_map

print(max_value_key({'a': 10, 'b': 20, 'c': 5}))