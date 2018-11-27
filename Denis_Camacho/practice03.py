number = int(input("into the number"))

odd_ever = lambda x: "The number is even" if x % 2 == 0 else "The number is odd"
print odd_ever(number)
