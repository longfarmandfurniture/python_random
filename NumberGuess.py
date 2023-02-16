import random

def main():
    guessed_number = input("Pick a nuber between 1 and 10: ")
    if guessed_number.isnumeric() == False:
        print("That is not a number.")
        exit(0)
    guessed_number = int(guessed_number)
    if guessed_number < 1:
        print("That number is too low.")
        exit(0)
    if guessed_number > 10:
        print("That number is too high.")
        exit(0)

    random_number = random.randint(1,10)
    #print(random_number)

    if(guessed_number < random_number):
        print(f"Your guess was too low, the number was {random_number}.")
        exit(0)

    if(guessed_number > random_number):
        print(f"Your guess was too high, the number was {random_number}.")
        exit(0)

    if(guessed_number == random_number):
        print(f"Good guess!  The number was {random_number}.")


if __name__ == "__main__":
    main()