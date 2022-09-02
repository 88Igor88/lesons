age_1 = input("Первое число:")
age_1 = int(age_1)
age_2 = input("Второе число")
age_2 = int(age_2)
ope = input("Введите оператор")
if ope == "+":
    print(age_1 + age_2)
elif ope == "*":
    print(age_1 * age_2)
elif ope == "-":
    print(age_1 - age_2)
elif ope == "//":
    print(age_1 // age_2)
elif ope == "%":
    print(age_1 % age_2)    
elif ope == "/":
    print(age_1 / age_2)
elif ope == "**":
    print(age_1 ** age_2)
