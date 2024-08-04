def run_length_encoding(s):
    if not s:
        return ""
    
    encoded_str = ""
    count = 1
    previous_char = s[0]
    
    for char in s[1:]:
        if char == previous_char:
            count += 1
        else:
            encoded_str += f"{previous_char}{count}"
            previous_char = char
            count = 1
    
    encoded_str += f"{previous_char}{count}"
    return encoded_str

input_str = input("Enter the string: ")
result = run_length_encoding(input_str)
print(result)
