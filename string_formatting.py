
#padding
print("{:8.3f}".format(1112.23))
print("{:8.3f}".format(-1112.23))
# show  + sign
print("{:+08.3f}".format(1112.23))
print("{:+08.3f}".format(-1112.23))

# show  only  - sign
print("{:-08.3f}".format(1112.23))
print("{:-08.3f}".format(-1112.23))

# show space for + sign
print("{: 08.3f}".format(1112.23))
print("{: 08.3f}".format(-1112.23))

# Center aligned
print("{:^ 018.3f}".format(1112.23))
print("{:^ 018.3f}".format(-1112.23))


print("{:*^5}".format("cat"))
