from calendar import monthrange

# Write a function days_in_month which takes the name of a month, and returns the number of days in the month.


def days_in_month(name):
    month = -1
    if name.lower() == "january":
        month = 1
    if name.lower() == "february":
        month = 2
    if name.lower() == "march":
        month = 3
    if name.lower() == "april":
        month = 4
    if name.lower() == "may":
        month = 5
    if name.lower() == "june":
        month = 6
    if name.lower() == "july":
        month = 7
    if name.lower() == "august":
        month = 8
    if name.lower() == "september":
        month = 9
    if name.lower() == "october":
        month = 10
    if name.lower() == "november":
        month = 11
    if name.lower() == "december":
        month = 12
    if month > -1:
        return monthrange(2018, month)[1]
    else:
        return None


if __name__ == '__main__':
    print "Enter name of the month:"
    mn = str(raw_input())
    cant = days_in_month(mn)
    if cant is None:
        print "Invalid name."
    else:
        print "RESULT: ", cant
