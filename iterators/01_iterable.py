numbers = [1,4,9]
methods = dir(numbers)
if '__iter__' in methods:
    print('list is an iterable')

value = iter(numbers) // numbers.__iter__()

item1 = next(value)

print(item1)
