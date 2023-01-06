from validator_collection import checkers

inp_email = input("What's your email address? ")
if checkers.is_email(inp_email):
    print("Valid")
else:
    print("Invalid")