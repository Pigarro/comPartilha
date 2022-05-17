print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
names = name1.lower() + name2.lower()
print(type(names), names)

true_count = 0 
true_count += names.count("t")
true_count += names.count("r")
true_count += names.count("e")
true_count += names.count("u")

print(true_count)

love_count = 0 
love_count += names.count("l")
love_count += names.count("o")
love_count += names.count("v")
love_count += names.count("e")

print(love_count)

loveScore = int(str(true_count) + str(love_count))


print(loveScore)

if (loveScore < 10) or (loveScore > 90):
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif (loveScore >= 40) and (loveScore <= 50):
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")