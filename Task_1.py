password =  str(input("Введите пароль"))
passwordChesk = str(input("Повторите пароль"))
if password == passwordChesk:
    print("Пароль принят")
else:
    print("Пароль не принят")