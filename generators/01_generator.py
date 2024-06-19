def all_even():
    n = 0
    while True:
        yield n
        n += 2

gen = all_even()
while True:
    print(next(gen))