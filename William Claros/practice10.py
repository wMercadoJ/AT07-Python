# Function 1:
# No arguments defined
# Should ask to the user the number of elements in the list
# According the value inserted ask for each value of the array and push it in a new array
# Return the array
def function1():
    array_size = int(input("Enter the size that the fix will have: "))
    array = []
    for auxiliary in range(array_size):
        new_number = int(input("Enter a number: "))
        array.append(new_number)
    return array


# Function 2
# Should receive 1 argument (the array returned in method 1)
# should print the array
def function2(list):
    print list

list = function1()
function2(list)