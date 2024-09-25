# Ethan Lawrence
# September 25 2024
# Simple Math

# Input
num1 = int(input('Please Input a number:    '))
num2 = int(input('Please Input a Second number:    '))

# Process
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2

# Output
print(f'The SUM of {num1} and {num2} is:        {sum}.')
print(f'The DIFFERENCE of {num1} and {num2} is: {difference}.')
print(f'The PRODUCT of {num1} and {num2} is:    {product}.')
print(f'The QUOTIENT of {num1} and {num2} is:   {quotient}.')
print(f'The MODULUS of {num1} and {num2} is:    {remainder}. \n')


# Part 2

# input
length = float(input('Please enter the length of the room in feet:  '))
width = float(input('Please enter the width of the room in feet:  '))

# Process
area = str(width * length) + 'ft\u00b2'

# Output
print(area + '\n')


# Part 3

# A
# Input
name = input('Input your name please:   ')
age = int(input('Input your age please:    '))
fav_color = input('Input your favorite color please:  ')

# Process
message = "My name is {0}, I am {1} years old, and my favorite color is {2}.".format(name, age, fav_color)

# Output
print(message)

# B
# Input
tax = 0.06
order_cost1 = float(input('What is the cost of this item:     '))
order_cost2 = float(input('What is the cost of this item:     '))
order_cost3 = float(input('What is the cost of this item:     '))

# Process
grand_total = order_cost1 + order_cost2 + order_cost3 + ((order_cost1 + order_cost2 + order_cost3) * tax)

# Output
print(tax)
print(f"The grand total of these items is ${grand_total:,.2f}")

# C
# Input
friend_name = input('input your best friend\'s name:   ')
friend_school = input('input the school that your best friend attends:  ')

# Output
print("your best friend {0} attends {1}.".format(friend_name, friend_school))