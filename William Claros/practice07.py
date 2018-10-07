# Write a function days_in_month which takes the name of a month, and returns the number of days in the month. Ignore leap years:
# 		days_in_month("February") == 28   days_in_month("December") == 31
# If the function is given invalid arguments, it should return None.
def days_in_month(name_month):
    return {
        'January': "31 days",
        'February': "28 days",
        'March': "31 days",
        'April': "30 days",
        'May': "31 days",
        'June': "30 days",
        'July': "31 days",
        'August': "31 days",
        'September': "30 days",
        'Octuber': "31 days",
        'November': "30 days",
        'December': "31 days",
    }.get(name_month, "Invalid month option, please try again.")

month = raw_input("Enter a month of the year: ")
print (days_in_month(month))
