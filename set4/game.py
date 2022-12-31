import random as rd

while True:
    num = input("Level: ")
    try:
        n = int(num)
        if n >= 0:
            break
        else:
            continue
    except ValueError:
        continue
number = rd.randrange(1, n)
while True:
    while True:
        _guess = input("Guess: ")
        try:
            guess = int(_guess)
            break
        except ValueError:
            continue
    if guess - number == 0:
        print("Just right!")
        break
    elif guess - number > 0:
        print("Too large!")
        continue
    elif guess - number < 0:
        print("Too small")
        continue
