def sum_of_odd_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            total += num
    return total

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

sum_odd = sum_of_odd_numbers(start, end)

print(f"The sum of all odd numbers between {start} and {end} is: {sum_odd}")
