place = int(input("Введите номер вашего места"))
if place > 52 or place < 1:
    print("Неверное значение")
else:
    if place % 2 == 0:
            if int(place) >= 36:
                print("Ваше место верхнее, боковое")
            else:
                print("Ваше место нижнее, боковое")
    else:
        if int(place) > 36:
            print("Ваше место верхнее, купе")
        else:
            print("Ваше место ниижнее, купе")
