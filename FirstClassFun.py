def divide(divi, deve):
    if divi == 0:
        raise ZeroDivisionError("Divi cannot be Zero")

    return divi / deve


def calcu(*value, operator):
    return operator(*value)

result = calcu(20, 78, operator=divide)
print(result)