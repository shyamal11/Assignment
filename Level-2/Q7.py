def find_median(number_list):
    number_list.sort()
    n = len(number_list)
    mid = n // 2
    if n % 2 == 0:
        return (number_list[mid - 1] + number_list[mid]) / 2
    else:
        return number_list[mid]

number_list = list(map(int, input("Enter numbers separated by space: ").split()))

median = find_median(number_list)

print(f"Median: {median:.1f}")
