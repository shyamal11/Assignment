def rotate_array(arr, d):
    n = len(arr)
    d = d % n  # Handle rotation greater than array length
    return arr[-d:] + arr[:-d]

arr = list(map(int, input("Enter elements of the array separated by space: ").split()))
d = int(input("Enter the number of rotations: "))

rotated_array = rotate_array(arr, d)

print(f"Array after rotation: {rotated_array}")
