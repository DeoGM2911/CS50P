def main():
    fuel_remained = input('Fraction: ')
    print(gauge(convert(fuel_remained)))


def convert(fraction: str) -> int:
    nums = fraction.split('/')
    x = int(nums[0])
    y = int(nums[1])
    _percent = (x / y) * 100
    if _percent > 100:
        raise ValueError
    return _percent


def gauge(percent: float) -> str:
    if percent <= 1:  # Empty
        return 'E'
    elif percent >= 99:  # Full
        return 'F'
    else:
        if percent - int(percent) >= 0.5:
            return f'{percent + 1}%'
        else:
            return f'{percent}%'

if __name__ == "__main__":
    main()
