import random

secret = random.randint(1, 10)
attempts = 0

with open("score.txt", "r") as score_file:
    score = int(score_file.read())
    best_score = str(score)
    print("Top score: {0}" .format(best_score))

# endless loop
while True:
    guess = int(input("Please guess the secret number between 1 and 10: "))
    attempts += 1    #+= adds a number to a variable, changing the variable itself in the process

    if guess == secret:
        print("Congratulations! Secret number is number " + str(secret) + ".")
        print("Attempts needed: {0}" .format(attempts))    #format method to join 2 strings
        attempts = str(attempts)
        if attempts < best_score:    #only save best result
            with open("score.txt", "w") as score_file:
                score_file.write(attempts)
        break  # break the loop

    elif guess > 10:
        print("Choose number between 1 and 10!")

    elif guess > secret:
        print("Your guess is not correct. Try something smaller.")

    elif guess < secret:
        print("Your guess is not correct. Try something bigger.")
