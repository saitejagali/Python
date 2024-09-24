#Write a function find_common_elements(lst1, lst2) that takes two lists and returns a new list containing elements that are common between both lists (use the in keyword).

def find_common_elements(lst1, lst2):
    new_list = []
    for i in lst1:
        if i in lst2:
            new_list.append(i)  # Append the element directly
    return new_list  # Return the list of common elements

# Example usage
print(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
