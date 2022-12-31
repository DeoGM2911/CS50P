def main():
    greet = input("How's it going? ")
    print(f"${value(greet)}")


def value(greeting: str):
    if greeting.lower() == 'hello':
        return 0
    elif greeting.lower().startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()