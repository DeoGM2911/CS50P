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
    Order = input("Items: ")
    if Order == '': # control - d
        break
    # convert the input in to title cased form
    if Order.title() in menu.keys():
        bill = bill + menu[Order.title()]
        print(f'Total: {bill}$')
        continue
    else:
        continue
