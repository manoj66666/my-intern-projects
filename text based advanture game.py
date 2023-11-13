import time

def introduction():
    print("Welcome to the Text-based Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious land...")
    time.sleep(1)
    print("Make choices to determine your fate!")

def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            user_input = int(input("Enter the number of your choice: "))
            if 1 <= user_input <= len(choices):
                return user_input
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def chapter_one():
    print("Chapter One: The Beginning")
    time.sleep(1)
    choices = ["Enter the dark cave.", "Follow the mysterious path."]
    user_choice = make_choice(choices)

    if user_choice == 1:
        print("You enter the dark cave...")
        time.sleep(1)
    elif user_choice == 2:
        print("You follow the mysterious path...")
        time.sleep(1)

def main():
    introduction()
    chapter_one()

if __name__ == "__main__":
    main()
