import inflect
p = inflect.engine()
# To solve the problem we use the join() method


def main():
    """
    Returns: the lyrics with the grammatically correct version of the list of names
    """
    # At least one name so no issue
    list_of_name = insert_name()
    # if len(list_of_name) < 1:
    #   print("Say goodbye to your friends!")
    lyrics = p.join(list_of_name)
    print(f"Adieu, adieu, to {lyrics}")


def insert_name():
    """
    Returns: a list of names inputted by the user
    """
    list_name = list()
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            break
        if len(name) < 1:
            break
        list_name.append(name)
    return list_name


if __name__ == "__main__":
    main()

