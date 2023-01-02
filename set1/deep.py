answer = input('What is your answer to the question of Life, Universe, and Everything?\n')
if answer == '42':
    print('Oh my god!')
elif (answer.lower() in ['forty-two','forty two']):
    print('Oh my god!')
else:
    print('No!')
