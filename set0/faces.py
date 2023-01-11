def convert(text: str):
    new_text = text.replace(':)', '😀')
    new_text = new_text.replace(':(', '🙁')
    return new_text


def main():
    text = input()
    print(convert(text), end="")


main()