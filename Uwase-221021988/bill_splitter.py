#  Names: UWASE Marie Claire
#  Department:Computer Science
#  Reg num:221021988
import random

friend = input("Enter the number of friends joining (including you):\n")
num = int(friend)
users_dict = {}

if num > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for n in range(num):
        name = input()
        users_dict.update({name: 0})
    
    print("Enter the total bill value:")
    x = input()
    bill = int(x)
    for_each = int(bill) / num
    for key,value  in users_dict.items():
        users_dict[key] = round(for_each, 2)

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: \n")
    select = input()
    if select == "Yes":
        luck_one = random.choice(list(users_dict))
        print(luck_one, " is the lucky one!")

        for_remaining = bill / (num - 1)

        for key,value  in users_dict.items():
            if key == luck_one:
                users_dict[luck_one] = 0
            else:
                users_dict[key] = round(for_remaining, 2)
        print(users_dict)
    else:
        print("No one is going to be lucky")
        print(users_dict)
else:
    print("No one is joining for the party")
