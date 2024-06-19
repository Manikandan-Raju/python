'''Write a Python program that prints the numbers from 1 to 100. 
But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz".
For numbers that are multiples of both three and five, print "FizzBuzz".'''

for i in range(1,101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if not output:
        output = str(i)
    print(output)
    