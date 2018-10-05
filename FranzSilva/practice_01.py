class PerformOp:
    franz_silva_elmer_milan = "varaible long name"
    franz2018_silva_milan = 2018

    def __init__(self):
        self.sum = 0
        self.rest = 0
        self.multi = 0
        self.div = 0.0

    def operation(self, number_1, number_2):
        self.sum = number_1 + number_2
        print("suma es: ", self.sum)
        self.rest = number_1 - number_2
        print("rest es: ", self.rest)
        self.multi = number_1 * number_2
        print("multiplicacion es: ", self.multi)
        self.div = number_1 / number_2
        print("division es: ", self.div)
