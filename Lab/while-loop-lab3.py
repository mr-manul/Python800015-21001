import random

number = random.randint(1, 10)

while True:
    guess = int(input("type number between 1 and 100: "))
    if guess == number:
        print("you guessed right!")
        break
    elif guess < number:
        print("too low")
        continue
    elif guess > number:
        print("too high")
        continue


