import random

secret = random.randint(1, 10)
guess = 0

# endless loop
while True:
    guess = int(input("Please guess the secret number between 1 and 10: "))

    if guess == secret:
        print("Congratulations! Secret number is number " + str(secret) + ".")
        break  # break the loop
    elif guess > 10:
        print("Choose number between 1 and 10!")
    elif guess > secret:
        print("Your guess is not correct. Try something smaller.")
    elif guess < secret:
        print("Your guess is not correct. Try something bigger.")
