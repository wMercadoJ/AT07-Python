def number_odd_even(num1):
     return ("odd") if (num1 % 2 == 0) else ("even")

num1 = int(input("Ingrese un numero "))
print (number_odd_even(num1))
