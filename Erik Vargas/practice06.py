month_input = str(input("insert month:"))


def cant_mes(month):
    month_of_year = {"january": 31, "february": 28, "march": 30, "april": 30, "may": 31, "june": 30,
                     "july": 30, "august": 31, "september": 31, "november": 31, "december": 31}

    for key in month_of_year:
        if month == key:
            print month_of_year[key]


cant_mes(month_input)
