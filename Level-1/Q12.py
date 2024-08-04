def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num

number = int(input("Enter a number: "))

reversed_number = reverse_number(number)

print(f"The reversed number is: {reversed_number}")
