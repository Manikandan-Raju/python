from copy import deepcopy

# create a list from a generator expression
# this is equivalent to list(range(50))
original = list(i for i in range(50))
print("original length:", len(original))
print("original sample:", original[:5], "...")

# create another list from 50 to 60 inclusive
more_numbers = list(i for i in range(50, 61))
print("more_numbers:", more_numbers)

# deepcopy returns an independent copy
copied = deepcopy(original)
print("copied length before extend:", len(copied))

# append() adds one element at the end and returns None
append_result = original.append(more_numbers)
print("after original.append(more_numbers):")
print("  original length:", len(original))
print("  last element is the appended list:", original[-1] == more_numbers)
print("  append returned:", append_result)

# extend() adds each element from the iterable to the list and also returns None
extend_result = copied.extend(more_numbers)
print("after copied.extend(more_numbers):")
print("  copied length:", len(copied))
print("  copied tail sample:", copied[-6:])
print("  extend returned:", extend_result)

# len() still works after extend
print("len(copied):", len(copied))

# append a single element, then remove it
copied.append(60)
print("after copied.append(60):", copied[-6:])
remove_result = copied.remove(60)
print("after copied.remove(60):", copied[-6:])
print("remove returned:", remove_result)

# create a tuple from a generator expression
# tuple is immutable, unlike list
t = tuple(i for i in (1, 2, 3))
print("tuple t:", t)

# clear empties the list in-place
copied.clear()
print("copied after clear():", copied)
