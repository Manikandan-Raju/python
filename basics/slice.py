my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']

# # items from index 2 to index 4
# print(my_list[2:5])

# print(my_list[5:2:-1])

# # items from index 5 to end
# print(my_list[5:])

# # items beginning to end
# print(my_list[:])


s = 'amazingjob'
#print ram
print(my_list[-3::1])
print(my_list[-3::-1])
print(my_list[1:15:-1])
print(my_list[:-3:1])
print(my_list[:-3:-1])
print(my_list[0:-3:1])
print(my_list[-3:-8:1])
print(my_list[-3:-7:-2])
print(my_list[-8:-3:1])
print(my_list[4:1:1])
print(my_list[4:1:-1])
# print(my_list[15])


for i in range(15):
    print(i)
    if i >= len(my_list):
        # raise(SystemExit)
        # raise(IndexError)
        raise(StopIteration)
        
    print(my_list[i])

    print('i')
