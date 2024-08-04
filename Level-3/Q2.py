def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    return len(lines)

filename = 'demo.txt'
print(f"Number of lines in {filename}: {count_lines(filename)}")
