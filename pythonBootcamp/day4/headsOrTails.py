import random

print(f"""This is a heads or tails game.""")
computer = random.randint(1, 2)
player = int(input("""Choose 1 for heads or 2 for tails:  """))

if player == computer:
    print("You guess it right!")
else:
    print("Better luck next time")