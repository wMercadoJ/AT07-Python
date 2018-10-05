# Create 1 script to determine is a number is odd or even
# (use single line statement if applies)


def method_number_pair_odd(value1):
    return "It is number pair" if (value1 % 2 == 0) else "It is number odd"


first_value = int(input("Enter a positive integer: "))

print(method_number_pair_odd(first_value))