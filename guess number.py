

import random

secret_number = random.randint(1, 100)

# print(secret_number)

guess = 0

while guess != secret_number:
    guess = int(input("Угадай число от 1 до 100: "))

    if guess < secret_number:
        print("Загаданное число больше!")
    elif guess > secret_number:
        print("Загаданное число меньше!")
    else:
        print("Поздравляю! Ты угадала!")