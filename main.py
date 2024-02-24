from random import randint
from datetime import datetime

time_now = datetime.now()


def win_game():
    with open('log.txt', 'a', encoding='utf-8') as file_win_game:
        line_end = f'[{time_now}][INFO][System]: Число угадано!\nПопыток:{attempts}'
        file_win_game.write(f'{line_end}\n')


def entered_number():
    with open('log.txt', 'a', encoding='utf-8') as file_entered:
        line_entered = f'[{time_now}][INFO][User]: Введено число: {user_number}'
        file_entered.writelines(str(line_entered) + '\n')


while True:
    list_more_numbers = []
    list_less_numbers = []
    all_numbers = {'Больше': list_less_numbers, 'Меньше': list_more_numbers}
    print("--------------------------------")
    print(f'Это простая игра - "Угадай число"')

    with open('log.txt', 'a', encoding='utf-8') as file:
        computer_number = randint(1, 100)
        line = f'[{time_now}][INFO][System]: Загадано число: {computer_number}'
        file.writelines(str(line) + '\n')
    print("Число загадано!")
    print("________________________________")
    attempts = 0
    while True:
        try:
            user_number = int(input("Введи число от 1 до 100 (невключительно): "))
        except ValueError:
            print(f'Вы ввели текстовое значение, а нужно число!')
            break
        print(computer_number)
        if computer_number > user_number:
            print("Не угадал! Загаданное число больше!")
            attempts += 1
            list_more_numbers.append(user_number)
            print(list_more_numbers)
            entered_number()

        elif computer_number == user_number:
            attempts += 1
            print(f'Вы угадали число! Количество пыпыток, которое вам потребовалось для отгадывания числа: {attempts}')
            print(f'________________________________')
            print(f'Все введеные числа при отгадывании!')
            print(all_numbers)
            win_game()
            break
        else:
            print("Не угадал! Загаданное число меньше!")
            attempts += 1
            list_less_numbers.append(user_number)
            print(list_less_numbers)
            entered_number()
