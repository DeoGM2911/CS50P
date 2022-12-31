def main():
    price = price_as_float(input('How much was the meal? \n'))
    tip = price * percent_as_float(input('What percentage will you tip? \n'))
    bill = price + tip
    print(f'Your total bill is ${bill}')

def price_as_float(price: str):
    price = price.replace('$', '')
    return float(price)

def percent_as_float(percent_tip: str):
    percent_tip = percent_tip.replace('%', '')
    return float(percent_tip)/100

main()