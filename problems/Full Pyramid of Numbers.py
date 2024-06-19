"""
        1 
      2 3 2 
    3 4 5 4 3 
  4 5 6 7 6 5 4 
5 6 7 8 9 8 7 6 5
                    """
n = 5

for i in range(n):
    print(' ' * (n - i ), end = '' )
    print(str(i+1) * (2 *i +1), end = '' )
    print()

for i in range(n):
    for j in range(n-i):
        print(' ', end = '' )
    for j in range((i +1)):
        print(str(i+j+1)  , end = '' )
    for j in range((i)):
        print(str(2*i -j)  , end = '' )
    print()