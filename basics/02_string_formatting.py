"""String formatting examples with padding, sign, and alignment.

This file shows how Python's `str.format()` uses format specifiers
with width, precision, sign control, zero fill, and alignment.
"""

print("# padding to width 8 with 3 decimals")
print("{:8.3f}".format(1112.23))  # -> '1112.230'
print("{:8.3f}".format(-1112.23)) # -> '-1112.230'

print("\n# show leading zero padding with explicit sign")
print("{:08.3f}".format(2.23))   # -> '+002.230'
print("{:08.3f}".format(-2.23))  # -> '-002.230'

print("\n# show plus sign for positives and sign for negatives")
print("{:+08.3f}".format(12.23))  # -> '+12.230'
print("{:+08.3f}".format(-12.23)) # -> '-12.230'

print("\n# show only negative sign, positive numbers have no sign")
print("{:-08.3f}".format(12.23))  # -> '12.230'
print("{:-08.3f}".format(-12.23)) # -> '-12.230'

print("\n# show only negative sign, positive numbers have no sign")
print("{:-08.3f}".format(12.23))  # -> '00012.230'
print("{:-8.3f}".format(-12.23))  # -> ' -12.230'

print("\n# show space for positive sign, negative still gets '-' ")
print("{: 8.3f}".format(1112.23))  # -> ' 1112.230'
print("#{: 8.3f}#".format(-1112.23)) # -> '-1112.230'

print("\n# right aligned (default) within width 8")
print("{:8.3f}".format(2.23))      # -> '   2.230'
print("{:8.3f}".format(-2.23))     # -> '  -2.230'

print("\n# left aligned within width 8")
print("{:<8.3f}".format(2.23))     # -> '2.230   '
print("{:<8.3f}".format(-2.23))    # -> '-2.230  '

print("\n# center aligned within width 8")
print("{:^8.3f}".format(2.23))     # -> ' 2.230  '
print("{:^8.3f}".format(-2.23))    # -> ' -2.230 '

print("\n# f-string formatting examples")
value = 2.23
print(f"{value:8.3f}")    # right aligned, width 8, 3 decimals -> '   2.230'
print(f"{value:<8.3f}")   # left aligned -> '2.230   '
print(f"{value:^8.3f}")   # centered -> ' 2.230  '

print("\n# f-string with explicit sign and zero fill")
print(f"{value:+08.3f}")  # -> '+002.230'
print(f"{-value:+08.3f}") # -> '-002.230'

print("\n# literal braces in f-strings")
print(f"{{value:8.3f}}")   # prints '{value:8.3f}'


