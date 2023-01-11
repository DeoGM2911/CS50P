answer = input('What is your answer to the question of Life, Universe, and Everything?\n')
if answer.strip() == '42':
    print('Yes', end="")
elif (answer.lower() in ['forty-two','forty two']):
    print('Yes', end="")
else:
    print('No', end="")
