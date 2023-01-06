from validator_collection import checkers

inp_email = input("What's your email address? ")
if checkers.is_email(inp_email):
    print("Valid")
else:
    print("Invalid")

# Just a note. The regex of email is:
# ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+ -> username
# @[a-zA-Z0-9] -> @ and domain
# (?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9]) -> additional info about domain
# (?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$