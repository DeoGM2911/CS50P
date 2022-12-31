import emoji
plain_text: str = input("Text: ")
emojy: str = emoji.emojize(plain_text, language='alias', variant=None)
print(f"Output: {emojy}")


