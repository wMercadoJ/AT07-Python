# Practice 07
# author Ana Mamani
# since 10/05/2018

def days_in_month(month):
    month_day = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
                 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

    for i in month_day.keys():
        if month == i:
            return month_day[month]


print(days_in_month("November"))
