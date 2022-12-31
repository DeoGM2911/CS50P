camel_name = input("What is the variable's name? \n")
snake_name = ''
def change(camel_name: str):
    for char in camel_name:
        if char.islower():
            snake_name = snake_name + char
        else:
            snake_name = snake_name + '_' + char.lower()
    return snake_name
print(snake_name)