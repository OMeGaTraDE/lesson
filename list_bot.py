charge = []
bot = input("введите командую.. ")
while bot != "выход":
    if bot == "добавить":
        oo = int(input("ведите число "))
        charge.append(oo)
    elif bot == "удалить":
        ind = int(input("какой элемент удалить? "))
        if len(charge) > ind:
            del charge[ind]
        else:
            print("такого элемента нет")
    elif bot == "список":
        print(charge)
    else:
        print("такой команды нет!")
    bot = input("введите командую.. ")
print(charge)
