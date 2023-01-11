import random as rd

while True:
    num = input("Level: ")
    try:
        n = int(num)
        if n > 0:
            break
        else:
            continue
    except ValueError:
        continue
number = rd.randrange(1, n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        continue
    if guess - number == 0:
        print("Just right!")
        break
    elif guess - number > 0:
        print("Too large!")
    elif guess - number < 0:
        print("Too small!")
