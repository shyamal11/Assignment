def sum_of_digits(n):
    while n >= 10:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        n = total
    return n

number = int(input("Enter a number: "))

result = sum_of_digits(number)

print(f"The single-digit sum is: {result}")
