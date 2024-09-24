'''9. Check if Two Strings are Rotations of Each Other
Question: Check if one string is a rotation of another string.'''

def are_rotations(s1, s2):
    return len(s1)==len(s2) and s2 in s1+s1

print(are_rotations("waterbottle", "erbottlewat"))