# угадай число
import random
random_number = random.randrange(1, 100)
user_guess  = -1
guess_mode = 0
while user_guess != random_number:
    user_guess=int(input("Угдайте число от 1 до 100"))
    guess_mode += 1
    if user_guess > random_number:
        print('Число должно быть меньше')
    elif(user_guess < random_number):
        print('Число должно быть больше! ')
    else:
        game_again = input(f'Вы угадали, это число = {user_guess}, вы угадали с {guess_mode} попытки, желаете продолжить?')
        if game_again == 'no' or game_again == 'нет' or game_again == 0 or game_again == '':
            break
        elif game_again:
            guess_mode = 0
            random_number = random.randrange(1, 100)
        else:
            break