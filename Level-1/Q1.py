# If a number is divisible by 3 it should print “Consultadd” as a string 

def check_divisibility(number):
    if number % 3 == 0:
        print("Consultadd")

if __name__ == "__main__":
    # Take input from the user
    try:
        number = int(input("Enter a number: "))
        check_divisibility(number)
    except ValueError:
        print("Please enter a valid integer.")


# If a number is divisible by 5 it should print “Python Training” as a string

def check_divisibility(number):
    if number %  5== 0:
        print("Python Training")

if __name__ == "__main__":
    # Take input from the user
    try:
        number = int(input("Enter a number: "))
        check_divisibility(number)
    except ValueError:
        print("Please enter a valid integer.")



#If a number is divisible by both 3 and 5 it should print
#“Consultadd - Python Training” as a string.


def check_divisibility(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Consultadd - Python Training")

# Take input from the user
try:
    number = int(input("Enter a number: "))
    check_divisibility(number)
except ValueError:
    print("Please enter a valid integer.")



