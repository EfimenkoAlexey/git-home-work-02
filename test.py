result = None
operand = None
operator = None
wait_for_number = True
#--------------------------------------------------------------
result=0
while wait_for_number:
    try:
        operand = int(input("Введите число: "))
    except ValueError:
        print("Вы ввели не число.")
    else:
        print(operand)
        break
#----------------------------------------------------------------
result=operand
while wait_for_number:
    try:
        operator = (input("Введите математическую операцию: ")) 
    
    # вычисляем +
        if operator =="+":
            try:
                operand = int(input("Введите число: "))
                result = result + operand
            except ValueError:
                print("Вы ввели не число.")
            
            print(result)
    
    # вычисляем -
        elif operator =="-":
            try:
                operand = int(input("Введите число: "))
                result = result - operand
            except ValueError:
                print("Вы ввели не число.")
                operand = int(input("Введите число: "))
                result = result - operand
            print(result)
    
    # вычисляем *
        elif operator =="*":
            try:
                operand = int(input("Введите число: "))
                result = result * operand
            except ValueError:
                print("Вы ввели не число.")
            print(result)

    # вычисляем /
        elif operator =="/":
            try:
                operand = int(input("Введите число: "))
                result = result / operand
            except ZeroDivisionError:
                print("Ошибка. Деление на 0.")
            print(result)

    # заканчиваем цикл если =
        elif operator == "=":
            print(result)
            break
        else:
            print("Вы ввели не математическую операцию. Попробуйте еще раз.")
    except ValueError:
        print("Вы ввели не математическую операцию. Попробуйте еще раз.")  