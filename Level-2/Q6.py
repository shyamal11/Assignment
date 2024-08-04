def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

number = int(input("Enter a number: "))

print("Yes" if is_power_of_two(number) else "No")
