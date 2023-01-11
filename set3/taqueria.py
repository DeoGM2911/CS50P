menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
bill = 0
while True:
    try:
        Order = input()
    except EOFError:
        break
    if Order == '': # control - d
        break
    # convert the input in to title cased form
    if Order.title() in menu.keys():  # I used menu.keys() to avoid KeyError
        bill = bill + menu[Order.title()]
        print(f'Total: ${bill:2f}')
        continue
    else:
        continue