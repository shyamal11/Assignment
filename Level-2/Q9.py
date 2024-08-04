def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

lst = list(map(int, input("Enter elements of the list separated by space: ").split()))
index = int(input("Enter the index to access: "))

result = access_element(lst, index)

print(result)
