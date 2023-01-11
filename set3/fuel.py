# We can use the while loop to reprompt 
while True:
    # format: x/y
    nums = input('Fraction: ').split('/')
    # re-prompt the user for a fraction
    try:
        x = int(nums[0])
        y = int(nums[1])
        if x > y:  # Check for appropriate fraction
            print("Not a valid fraction! (Larger than 1)")
            continue
        percent = (x / y) * 100
        if percent <= 1:  # Empty
            print('E')
            break
        elif percent >= 99:  # Full
            print('F')
            break
        else:
            if int(percent) - percent < -0.5:
                print(f'{int(percent + 1)}%')
                break
            else:
                print(f'{int(percent)}%')
                break
    except ValueError:  # if x or y aren't integer then re-prompt
        print("x or y is not an integer!")
        continue
    except ZeroDivisionError:
        print("The denominator is 0!")
        continue