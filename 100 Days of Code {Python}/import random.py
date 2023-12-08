import random
names= ["Amine", "Karim", "Yassine"]


name = random.choice(names).lower()
len_of_name = len(name)

print(name)

display = list()

for index in range(len_of_name):
    display += "_"

guess = input("Guess a letter:")

for position in range(len_of_name):
    guess = input("Guess a letter:")
    letter = name[position]
    for element in name:
        if letter == guess:
            display[position] = element
    print(display)