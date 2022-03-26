# угадай число
import random
random_number = random.randrange(1, 100)
guess_mode = 0
while True:
    user_guess=int(input("Угдайте число от 1 до 100"))
    guess_mode += 1
    if user_guess > random_number:
        print('Число должно быть меньше')
    elif user_guess < random_number:
        print('Число должно быть больше! ')
    else:
        print(f'Вы угадали, это число = {user_guess}, вы угадали с {guess_mode} попытки')
        break