def split_string(string):
    return list(string)

input_list = input("Enter a list of strings ").strip().split(', ')
mapped_list = list(map(split_string, input_list))

print(mapped_list)
