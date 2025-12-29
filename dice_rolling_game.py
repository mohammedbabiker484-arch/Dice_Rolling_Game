import random

while True:
    choice = input("roll the dice?(y/n): \n ").lower()
    if choice == "y":
        num_1 = random.randint(1, 6)
        num_2 = random.randint(1, 6)
        print(f"({num_1} , {num_2})")
    elif choice == "n":
        print("thanks for playing!")
        break
    else:
        print("invalid choice")