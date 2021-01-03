# Write a Python function that takes a list 
# and returns a new list with unique elements of the first list.

def uniq_list(mylist):
    return list(set(mylist))

list_input = [1, 2, 3, 4, 3, 4, 2, 1, 3, 5, 3, 5]
print(list_input)
print(uniq_list(list_input))