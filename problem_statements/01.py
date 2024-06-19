# Write a program which takes a sequence of numbers and check if all numbers are unique.
l = [1,2,3,1]

print(any(True if v not in (l[:i] + l[i+1:]) else False for i,v in enumerate(l)) )

# Write a program for counting the number of every character of a given text file.
import collections, pprint

with open(r'python/problem_statements/sample.txt','r+') as f:
    data = f.read()
    counter ={}
    count_data = collections.Counter(data)
    count_value = pprint.pformat(count_data)
    for c in data:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
print(pprint.pformat(counter))
print(count_value)
