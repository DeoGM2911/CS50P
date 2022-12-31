amount_due = 50
print(f"Amount Due: {amount_due}")
while amount_due > 0:
    pay = int(input("Insert coin: "))
    if pay not in [25, 10, 5]:
        continue
    else:
        amount_due = amount_due - pay
        if amount_due <= 0:
            print(f"Change Owed: {0-amount_due}")
            break
        print(f"Amount Due: {amount_due}")