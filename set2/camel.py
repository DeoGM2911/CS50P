def main():
    print(change(input("What is the variable's name? \n")))


def change(camel_name: str):
    snake_name = ''
    for char in camel_name:
        if char.islower():
            snake_name = snake_name + char
        else:
            snake_name = snake_name + '_' + char.lower()
    return snake_name


if __name__ =="__main__":
    main()