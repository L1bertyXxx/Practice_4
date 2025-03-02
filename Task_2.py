place = int(input("Введите номер вашего места"))
if place % 2 == 0:
        if int(place) > 54:
            print("Ваше место верхнее, боковое")
        else:
            print("Ваше место нижнее, боковое")
else:
    if int(place) > 54:
        print("Ваше место верхнее, купе")
    else:
        print("Ваше место ниижнее, купе")
