def count_input(s):
    digits_count = 0
    letters_count = 0
    
    for char in s:
        if '0' <= char <= '9':
            digits_count += 1
        elif ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            letters_count += 1
    
    return digits_count, letters_count

user_input = input("Enter a string: ")

digits, letters = count_input(user_input)

print(f"Number of digits: {digits}")
print(f"Number of letters: {letters}")
