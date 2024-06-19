
'''
*
* *
* * *
'''


def left_pattern(m):
    for i in range(m):
        print('*' * (i+1),end='')
        print(' ' * (m-i-1) ,end= '')
        print("\n") 

def right_pattern(m):
    for i in range(m):
        print(' '* (m-i-1) ,end= '')
        print('*'* (i+1),end='')
        print("\n") 

def middle_pattern(m):
    for i in range(m):
        print(' '* (m - i -1) ,end= '')
        print('*'* (2*i +1),end='')
        print("\n") 

left_pattern(5)
right_pattern(5)
middle_pattern(5)