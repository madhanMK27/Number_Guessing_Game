import random

def play_game():
    print("\n🎮 Welcome to the Number Guessing Game!!!")
    print("I have selected a number between 1 and 100.")
    print("           Try to guess it")
    print("-------------------------------------------\n")
    print('Letss start !🎮\n')

    
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("🔽 Too low! Try again.\n")
            elif guess > secret_number:
                print("🔼 Too high! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.\n")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a number.\n")

def main():
    while True:
        play_game()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("👋 Thanks for playing!!")
            break


main()
