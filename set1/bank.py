# We can use a while loop test the code manually
greet = input("What's going? ").strip()
# if greet == '1':
#     break
if 'hello' in greet.lower():
    print("$0")
elif greet.lower().startswith('h'):
    print("$20")
else:
    print("$100")

