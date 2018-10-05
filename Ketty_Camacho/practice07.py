def days_in_month(month):
    all_months = {"January": 31,
              "February": 28,
              "March": 31,
              "April": 30,
              "May": 31,
              "June": 30,
              "July": 31,
              "August": 31,
              "September": 30,
              "October": 31,
              "November": 30,
              "December": 31}
    value = all_months.get(month)
    if (value == None):
        print "it is not correct month"
    else:
        print value


days_in_month("June")
