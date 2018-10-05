# Write a function sum_to(n) that returns the sum of all integer numbers up to and including only until any value lower than 35. So sum_to(10)wouldbe1+2+3...+10which would return the value 55, but if n=40 only until sum to 35 need to be returned.
def sum_to(number):
    sum = 0
    for auxiliar in range(number + 1):
        if auxiliar <= 35:
            sum += auxiliar
        else:
            break
    return sum

number = int(input("Enter one number: "))
print ("The summation of all the numbers up to " + str(number) + " is: " + str(sum_to(
    number)) + ", but only the sum up to number 35 is taken into account.")
