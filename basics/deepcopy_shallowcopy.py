# In Python, the assignment statement (= operator) does not copy objects. 
# Instead, it creates a binding between the existing object and the target variable name. 
# To create copies of an object in Python, we need to use the copy module. 
# Moreover, there are two ways of creating copies for the given object using the copy module -

# Shallow Copy
#     Shallow Copy is a bit-wise copy of an object. 
#     The copied object created has an exact copy of the values in the original object. 
#     If either of the values is a reference to other objects, just the reference addresses for the same are copied.
# Deep Copy
#     Deep Copy copies all values recursively from source to target object, 
#     i.e. it even duplicates the objects referenced by the source object.

from copy import copy, deepcopy
original_list = [1, 2, [3, 5], 4]
## shallow copy
shallow_copy_list = copy(original_list) 
shallow_copy_list[3] = 7
shallow_copy_list[2].append(6)
print(shallow_copy_list)    # output => [1, 2, [3, 5, 6], 7]
print(original_list)    # output => [1, 2, [3, 5, 6], 4]
## deep copy
deep_copy_list = deepcopy(original_list)
deep_copy_list[3] = 8
deep_copy_list[2].append(7)
print(deep_copy_list)    # output => [1, 2, [3, 5, 6, 7], 8]
print(original_list)    # output => [1, 2, [3, 5, 6], 4]

