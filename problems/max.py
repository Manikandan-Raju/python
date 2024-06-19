

def check_max(l):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max

m = check_max([424,4235,523512,2,525253,2525235252,525])
print(m)