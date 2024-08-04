def find_common_elements(l1, l2):
    common_elements = []
    for item in l1:
        if item in l2:
            common_elements.append(item)
    return common_elements

l1 = list(map(int, input("Enter elements of the first list : ").split()))
l2 = list(map(int, input("Enter elements of the second list : ").split()))

common_elements = find_common_elements(l1, l2)

print(f"Common elements: {common_elements}")
