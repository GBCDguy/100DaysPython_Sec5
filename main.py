"""for item in list_of_items:
        Do something for each item"""

fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(fruit)
    print(fruit + ' pie')
    print(fruits)

print(fruits)

student_scores = [180, 124, 165, 173, 189, 169, 146, 123, 142, 192, 158, 123]

''' Total score '''
total_score = sum(student_scores)
print(total_score)

total_score = 0
for score in student_scores:
    total_score += score
print(total_score)

''' Max score '''
max_score = max(student_scores)
print(max_score)

max_score = 0
for score in student_scores:
    if max_score < score:
        max_score = score
print(max_score)

''' Second max score '''
max_score = 0
for score in student_scores:
    if max_score < score:
        max_score = score
sec_max_score = 0
for score in student_scores:
    if sec_max_score < score < max_score:
        sec_max_score = score
print(sec_max_score)

""" Fizz Buzz """
upper_boundary = int(input("Upper Boundary: "))
for i in range(1, upper_boundary + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
        print(i)
    else:
        pass

"""Right angled triangle"""
height = 9
for i in range(0, height):
    print("*" * (i+1))

""" Equilateral triangle """
for i in range(1, height+1):
    print(' ' * (height - i), end='')
    print("*"*((2*i)-1))

""" Rhombus """
for i in range(1, round((height/2)+1)):
    print(' ' * (height - i), end='')
    print("*"*((2*i)-1))
for i in range(round((height/2)-1),0,-1):
    print(' '*(height - i), end='')
    print("*"*((2*i)-1))

""" Dice generator """
import random

dice_code = input("Dice code: ")

dice_data = dice_code[dice_code.index(' ') + 1:].split('d')
dice_num = int(dice_data[0])
dice_dots = int(dice_data[1])

dice = []
sum_dice = 0
for die in range(dice_num):
    dice.append(random.randint(1, dice_dots))
    sum_dice += dice[die]
print(dice)
print(sum_dice)

""" Password Generator """
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# TODO 1: Random pick letter, symbol, and number from list
password_list = []
for letter in range(nr_letters):
    password_list.append(random.choice(letters))
for symbol in range(nr_symbols):
    password_list.append(random.choice(symbols))
for number in range(nr_numbers):
    password_list.append(random.choice(numbers))
# TODO 2: Shuffle the list
random.shuffle(password_list)

# TODO 3: Converting the list into string
password = ''
for char in password_list:
    password += char
print(password)