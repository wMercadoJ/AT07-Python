# Create 1 script to determine is a number is odd or even (use single line statement if applies)
def is_even(number):
    return "This number is odd." if (number % 2 == 0) else "This number is even."

number = int(input("Enter a number to verify if it is even or odd: "))
print (is_even(number))
