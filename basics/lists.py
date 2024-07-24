from copy import deepcopy
l = list(i for i in range(50))


m = list(i for i in range(50,61))

j = deepcopy(l)
a = l.append(m)
e = j.extend(m)

print(l)
print(j)
print(len(j))
j.append(60)
print(j)
print(j.remove(60))
print(j)

t = tuple(i for i in (1, 2, 3))
print(t)

j.clear()
print(j)