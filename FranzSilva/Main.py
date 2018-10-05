from FranzSilva.practice_01 import PerformOp
from FranzSilva.practice_02 import Aritmetics

class Main:

    def main(self):
        perform = PerformOp()
        print("--------------------------------")
        print("Reults Values of practice 01")
        print("--------------------------------")
        print(perform.franz2018_silva_milan)
        print(perform.franz_silva_elmer_milan)
        perform.operation(1, 2)
        print("--------------------------------")
        print("Results practice 02")
        print("--------------------------------")
        artithmetic = Aritmetics()
        artithmetic.aritmetic_functions("-", 6, 5)


main = Main()
main.main()
