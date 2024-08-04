def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

list1 = list(map(int, input("Enter elements of the list separated by space: ").split()))

unique_list = unique_elements(list1)

print(f"List with unique elements: {unique_list}")
