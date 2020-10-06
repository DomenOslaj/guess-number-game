import random
import json
import datetime

secret = random.randint(1, 10)
attempts = 0

time = datetime.datetime.now()
current_time = time.strftime("%A " "%d-" "%m-" "%Y  " "%H:" "%M:" "%S")

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    #print(score_list)

for score_dict in score_list:
    #print(score_dict)
    print("Attempts: " + str(score_dict.get("attempts")) + " | " + "Date: " + score_dict.get("date"))


# endless loop
while True:
    guess = int(input("Please guess the secret number between 1 and 10: "))
    attempts += 1    #+= adds a number to a variable, changing the variable itself in the process

    if guess == secret:
        print("Congratulations! Secret number is number " + str(secret) + ".")
        print("Attempts needed: {0}" .format(attempts))    #format method to join 2 strings

        score_list.append({"attempts": attempts, "date": current_time})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break  # break the loop

    elif guess > 10:
        print("Choose number between 1 and 10!")

    elif guess > secret:
        print("Your guess is not correct. Try something smaller.")

    elif guess < secret:
        print("Your guess is not correct. Try something bigger.")