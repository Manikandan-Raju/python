# Reverse each word of a string
s = 'My Name is Jessa'

s = " ".join(i[::-1] for i in s.split(' '))

print(s)


def reverse_words_without_split(s):
    # Initialize an empty string to store the reversed words
    reversed_string = ""
    
    # Initialize a variable to keep track of the current word
    current_word = ""
    
    # Iterate over each character in the input string
    for char in s:
        if char != " ":
            current_word += char
        else:
            reversed_string += current_word[::-1] + " "
            current_word = ' '
    else:
        reversed_string += current_word[::-1] + " "
    return reversed_string


# Example usage
input_string = "Hello world, how are you?"
reversed_result = reverse_words_without_split(input_string)
print(f"Reversed string: {reversed_result}")
