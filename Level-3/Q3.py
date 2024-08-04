def JtoI(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    corrected_content = content.replace('J', 'I')
    
    print(corrected_content)

filename = 'words.txt'
JtoI(filename)
