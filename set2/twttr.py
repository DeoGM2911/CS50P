string = input("Input: ")
vowels = ['a', 'e', 'u', 'o', 'i', 'A', 'E', 'U', 'I', 'O']
new_string = string
for char in string:
    # This if-statement just make sure that the sentence will have meanings if it starts with a vowel like 'i'
    # if char == string[0]:
    # continue
    if char in vowels:
        new_string = new_string.replace(char, '')
print(new_string)
