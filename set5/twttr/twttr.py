def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word: str) -> str:
    """
    Shorten a word by removing vowels
    Args:
        word: a string inputted that may have vowels either upper or lower case
    Returns: a copy of the inputted word but without any vowels
    """
    vowels = ['a', 'e', 'u', 'o', 'i', 'A', 'E', 'U', 'I', 'O']
    shorten_word = word
    for char in word:
        # This if-statement just make sure that the sentence will have meanings if it starts with a vowel like 'i'
        # if char == word[0]:
        # continue
        if char in vowels:
            shorten_word = shorten_word.replace(char, '')
    return shorten_word


if __name__ == "__main__":
    main()
