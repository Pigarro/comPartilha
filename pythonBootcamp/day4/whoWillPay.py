import random

names_string = input("Give me everybodys's names, seperated by a comma.: ").lower()
names = names_string.split(", ")
print(names)

lucky_one = names[random.randint(0, len(names) - 1)]
for i in range(1):
    print(random.choice(names))


print(f"Today, {lucky_one.capitalize()} will pay the bill!")
print(f"Today, {random.choice(names)} will pay the bill tomorow!")