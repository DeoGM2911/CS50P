def main():
    price = price_as_float(input('How much was the meal? \n'))
    tip = price * percent_as_float(input('What percentage will you tip? \n'))
    print(f'Your total bill is ${price + tip}')


def price_as_float(price: str):
    return float(price.replace('$', ''))


def percent_as_float(percent_tip: str):
    return float(percent_tip.replace('%', ''))/100


main()