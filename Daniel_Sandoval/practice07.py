# Write a function days_in_month which takes the name of a month,
# and returns the number of days in the month. Ignore leap years:
# days_in_month ("February") == 28 days_in_month ("December") == 31
# If the function is given invalid arguments, it should return None.


def days_in_month(string):
    month = {'January': '31', 'February': '28', 'March': '31', 'April': '30',
             'Mach': '31', 'June': '30', 'July': '31', 'August': '30',
             'September': '31', 'October': '30', 'November': '31', 'December': '30'}
    for key in month.keys():
        if key.__contains__(string):
            return month[key]


string_month = raw_input("Insert a valid month: ")

print (days_in_month(string_month))