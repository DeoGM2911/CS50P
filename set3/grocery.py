dict_of_grocery = dict()

# generate the grocery list
while True:
    try:
        stuff = input().upper()
    except EOFError:
        break
    if len(stuff) == 0: 
        break #control-d 
    dict_of_grocery[stuff] = dict_of_grocery.get(stuff, 0) + 1
    
# Add stuff into the grocery list
list_of_grocery = list()
for item in dict_of_grocery.keys():
    list_of_grocery.append(f'{item}')

# sort the list
list_of_grocery.sort()

# Add occurences
for i in range(len(list_of_grocery)):
    print(f'{dict_of_grocery[list_of_grocery[i]]} {list_of_grocery[i]}', end="\n")