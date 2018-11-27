from Denis_Camacho import calculator_age, messages


def user_s():
    users = {}
    print("into the amount the user please")
    amount = int(input())
    for i in range(0, amount):
        print("INTO THE USER NAME PLEASE:")
        user_name = str(input())
        print("INTO THE AGE PLEASE:")
        age = int(input())
        users[user_name] = age

    for user_name, age in users.items():
        print(user_name)
        messages.message(age)
        calculator_age.calculator_age(age)


user_s()
