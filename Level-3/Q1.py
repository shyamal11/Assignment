def read_even_length_strings(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    even_length_strings = [line for line in lines if len(line.strip()) % 2 == 0]
    
    return ''.join(even_length_strings)

filename = 'doc.txt'
print(read_even_length_strings(filename))
