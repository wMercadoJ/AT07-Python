from FranzSilva.practice_01 import PerformOp
from FranzSilva.practice_02 import Aritmetics
from FranzSilva.PracticePython2 import NumberType
from FranzSilva.PracticePython3 import PythonTree


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
        print(artithmetic.aritmetic_functions("*", 6, 5))
        print("--------------------------------")
        print("impar o par results")
        print("--------------------------------")
        number_type = NumberType()
        print(number_type.is_odd_or_even(2), "2 par")
        print(number_type.is_odd_or_even(3), "3 impar")
        print("--------------------------------")
        print("primo results")
        print("--------------------------------")
        print(number_type.is_prime(7), "is prime?")
        print("--------------------------------")
        print("area of circle results")
        print("--------------------------------")
        print(number_type.area_of_circle(10))
        print("--------------------------------")
        print("sum to results")
        print("--------------------------------")
        print(number_type.sum_to(35))
        print("--------------------------------")
        print("days on moth to results")
        print("--------------------------------")
        print(number_type.days_in_month("April"))
        print("--------------------------------")
        print("url cut results")
        print("--------------------------------")
        print(number_type.cut_url("http://franz.com fra addddddd"))
        print("--------------------------------")
        print("replace  results")
        print("--------------------------------")
        practice_tree = PythonTree()
        print(practice_tree.repalce("franz e silva milan", "e", "Elmer"))
        print("--------------------------------")
        print("diccionarie  results")
        print("--------------------------------")
        print(practice_tree.count_concurrency("aaaaaa bb cc dd"))


main = Main()
main.main()
