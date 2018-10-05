from math import pi


class NumberType:
    def is_odd_or_even( self, number):
        return "even - par" if number % 2 == 0 else "odd - impar"

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def area_of_circle(self, radio):
        return pi*(radio**2) if radio > 10 else 0

    def sum_to( self, number ):
        sum = 630
        if number < 36:
            sum = 0
            for i in range(1, number + 1):
                sum += i
        return sum

    def days_in_month(self, month ):
        if month in ['September', 'April', 'June', 'November']:
            return 30

        elif month in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
            return 31

        elif month == 'February':
            return 28
        else:
            return None

    def cut_url( self, url):
        url_cuted = url.split(" ")
        for temp in url_cuted:
            return temp if "http" in temp else None
