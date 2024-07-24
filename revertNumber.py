needsToContinue = 'y'
while(needsToContinue.lower() == 'y') :
    try :
        userInput = int(input('Введите число: '))
        result = 0
        if userInput < 0 :
           result = abs(userInput)
        elif userInput > 0 :
           result = userInput - userInput * 2
        print('Результат: ' + str(result))
        needsToContinue = input('Продолжить?(y\\n): ')
    except :
        print('Это не число!')
