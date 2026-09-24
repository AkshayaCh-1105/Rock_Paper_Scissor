import random

print("===== ROCK PAPER SCISSORS =====")

player_score = 0
computer_score = 0

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("\n===== FINAL SCORE =====")
        print("Your score:", player_score)
        print("Computer score:", computer_score)
        print("Thank you for playing!")
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Please try again.")
        continue

    choices = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors"
    }

    player_choice = choices[choice]
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    print("\nYou chose:", player_choice)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a Draw!")

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or
        (player_choice == "Paper" and computer_choice == "Rock")
        or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("You Win! 🎉")
        player_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("Score:", player_score, "-", computer_score)