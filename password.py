finish = 'y'
while(finish.lower() == 'y') :
    password = 'Python'
    answer = input('Введите пароль: ')
    if answer == password :
        print('Пароль верный!')
        break
    elif answer != password :
        print('Неверный пароль.')
    finish = input('Хотите повторить попытку?(y\\n): ')
