input_string = input("Enter the string: ")
given_char = input("Enter the character: ")

starts_with_char = lambda s, c: s.startswith(c)

print(starts_with_char(input_string, given_char))
