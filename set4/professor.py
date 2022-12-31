import random as rd


def main():
    """
    Generate 10 problems, their answers , re-prompts, and returned messages and point
    """
    # generate level
    lvl = get_level()
    # generate problems and point
    point: int = 0
    for ques_index in range(0, 10):
        num_1 = generate_integer(lvl)
        num_2 = generate_integer(lvl)
        i = 1
        while i <= 4:
            # return the answer after three wrong answers
            if i == 4:
                print(f"{num_1} + {num_2} = {num_2 + num_1}")
                break
            # prompt the answer
            answer = input(f"{num_1} + {num_2} = ")
            try:
                # wrong answer then print EEE and re-prompt
                if int(answer) != num_1 + num_2:
                    print("EEE")
                    i += 1
                    continue
                # correct answer then add one point
                else:
                    point += 1
                    break
            # wrong answer then re-prompt
            except ValueError:
                print("EEE")
                i += 1
                continue
    print(f"Point: {point}")


def get_level():
    """
    Prompt the user for the number of digits in the questions
    Returns: the number of digits (aka. level) of numbers that are in the questions
    """
    level: int = 0
    while True:
        digit = input("Level: ")
        try:
            level = int(digit)
            if level == 1:
                return level
            elif level == 2:
                return level
            elif level == 3:
                return level
        except ValueError:
            continue


def generate_integer(_level: int):
    """
    Args:  _level - the number of digits of the numbers in the questions. Can only take value from the set [1, 2, 3]
    Returns: a randomly non-negative number with "level" digits
    """
    if _level == 1:
        number = rd.randint(0, 9)
    elif _level == 2:
        number = rd.randint(10, 99)
    elif _level == 3:
        number = rd.randint(100, 999)
    else:
        return ValueError
    return number

if __name__ == "__main__":
    main()
