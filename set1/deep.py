answer = input('What is your answer to the question of Life, Universe, and Everything?\n')
if answer == '42':
    print('Yes')
elif (answer.lower() in ['forty-two','forty two']):
    print('Yes')
else:
    print('No!')
