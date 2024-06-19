def string_length(string):
    count = 0
    for _ in string:
        count += 1
    return count

# Example usage
input_string = input("enter string: ")
length = string_length(input_string)
print("Length of the string:", length)
