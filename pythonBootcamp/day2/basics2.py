# Data types 

# String
name = "Sophia"
print(name[0])
print("sophia"[4])
# strings são tratadas como uma array

# Integer - number sem decimal

numbers = 123

print(numbers + 345) # ambos são do tipo number. soma é efetuada

#pode-se usar _(underscore) para fazer separação de big intergers
large_number = 123_345_445.569
print(large_number)
print(123,345.567) # dois numeros diferentes separados por vírgula

#Float
pi = 3.1415

#boolean - True or False
on = True
off = False


num_char = len(input("Qual o seu nome? "))
# print("Your name has " + num_char + " characters")  -> TypeError 
# cannot add or concatenar tipos diferentes de dados

print(num_char, type(num_char)) #quantidade de chars na string
# type() verifica o tipo do dado

print("Your name has " + str(num_char) + " characters")
# a conversão pode ser feita em uma variável, ou não

a = 123
print(type(a))
print(type(str(a)))
a = str(a)
print(type(a))
print(type(int(a)))
# a conversão pode ser feita em uma variável, ou não
b="100.5"
print(70 + float(b))
print(str(70) + b)

two_digit_number = input("Type a two digit number: ")
#print(int(num_a) + int(num_b))

num_a = int(two_digit_number[0])
num_b = int(two_digit_number[1])
print(num_a+num_b)

# + soma, - subtração, * multiplicação, / divisão(float) ** exponenciação
""" 
PEMDASLR

Parentheses     ()
Exponents       **
Multiplication  *       Divisão e multiplicação tem o mesmo peso
Division        /       da esquerda para a direita
Addition        +
Subtraction     -
Left to Rigth
"""

print(3/3+3*3/3)

# BMI calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


bmi = float(weight) / float(height) ** 2
print(int(bmi))

# BMI calculator in 1 line, no variables
print(f'Your BMI is: {int(float(input("enter your weight in kg: ")) / float(input("enter your height in m: ")) ** 2 )}')


# round() arredonda para o numero mais proximo
print(8/3)
print(round(8/3))
print(round(8/3, 2))
print(8//3)

result = 4 / 2
result /= 2
print(result)

score = 0 
score += 1
print(f'score {score}')

import datetime

now = datetime.datetime.now()
print(f'{now:%Y-%m-%d %H:%M}')

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


years_to_90 = 90 - int(age)
 

print(f"You have {int(years_to_90 * 3.154e+7):,} seconds, {years_to_90 * 525600:,} minutes, {years_to_90 * 8790:,} hours, {years_to_90 * 365:,} days, {years_to_90 * 52:,} weeks, and {years_to_90 * 12:,} months left.")