# 09_sets.py
# Sets are unordered collections of unique elements.

s = {1, 2, 3, 3, 4}
print("Set with duplicates removed:", s)

s.add(5)
print("After add(5):", s)

s.discard(2)
print("After discard(2):", s)

other = {3, 4, 5, 6}
print("Union:", s | other)
print("Intersection:", s & other)
print("Difference:", s - other)
print("Symmetric difference:", s ^ other)

# frozenset is an immutable set type useful for dictionary keys.
frozen = frozenset([1, 2, 3])
print("Frozen set:", frozen)
