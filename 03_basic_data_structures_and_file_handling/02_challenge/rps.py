import random

# choice_of_a = random.randint(1, 3)
# choice_of_b = random.randint(1, 3)

# print(choice_of_a, choice_of_b)

# 1:Rock, 2:Paper, 3:Scissors

#     a a a
#   - 1 2 3
# b 1 - a b
# b 2 b - a
# b 3 a b -

# if choice_of_a == choice_of_b:
#     print("Draw")
# elif (choice_of_a - choice_of_b) == 1:
#     print("A win")
# elif (choice_of_a - choice_of_b) == 2:
#     print("B win")
# elif (choice_of_b - choice_of_a) == 1:
#     print("B win")    
# else:
#     print("A win")

hands = ['rock', 'paper', 'scissors']

choice_of_a1 = random.choice(hands)
choice_of_b1 = random.choice(hands)

if choice_of_a1 == choice_of_b1:
    result = 'Draw'
elif (choice_of_a1 == 'rock' and choice_of_b1 == 'scissors') or (choice_of_a1 == 'scissors' and choice_of_b1 == 'paper') or (choice_of_a1 == 'paper' and choice_of_b1 == 'rock'):
    result = 'A1 win'
else:
    result = 'B1 win'

print('A1:' + choice_of_a1 + ', B1:' + choice_of_b1 + ', result:' + result)



