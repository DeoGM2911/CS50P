while True:
    greet = input("What's going? \n")
    if greet == '1':
        break
    if greet.lower() == 'hello':
        print("$0")
    elif greet.lower().startswith('h'):
        print("$20")
    else:
        print("$100")
    
