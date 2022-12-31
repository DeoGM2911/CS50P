while True:
    fuel_remained = input('Fraction: ')
    # format: x/y
    nums = fuel_remained.split('/')
    # re-prompt the user for a fraction
    try:
        x = int(nums[0])
        y = int(nums[1])
        if (x > y) or (y == 0):  # Check for appropriate fraction
            continue
        else:  # if the input is valid then break out of the 'prompt' loop
            break
    except ValueError:  # if x or y aren't integer then re-prompt
        continue
percent = (x / y) * 100
if percent <= 1:  # Empty
    print('E')
elif percent >= 99:  # Full
    print('F')
else:
    print(f'{int(percent)}%')
