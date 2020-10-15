import random
import json
import datetime


def play_game():
    name = input("I want to save you name, score and secret number. Could you tell me you name? ")
    secret = random.randint(1, 10)
    attempts = 0
    time = datetime.datetime.now()
    current_time = time.strftime("%A " "%d-" "%m-" "%Y  " "%H:" "%M:" "%S")
    score_list = get_score_list()

    for score_dict in top_score_list:
        text = "Attempts: {0} | Date and hour: {1} | Player: {2} | Secret number: {3} | Wrong guesses: {4}".format(str(
                                                                                                score_dict.get("attempts")),
                                                                                                score_dict.get("date"),
                                                                                                score_dict.get("name"),
                                                                                                score_dict.get("secret"),
                                                                                                score_dict.get(
                                                                                                    "wrong guesses"))
        print(text)

    wrong_guesses = []

    while True:
        guess = int(input("Please guess the secret number between 1 and 10: "))

        attempts += 1    # += adds a number to a variable, changing the variable itself in the process

        if guess == secret:
            print("Congratulations! Secret number is number " + str(secret) + ".")
            print("Attempts needed: {0}" .format(attempts))    # format method to join 2 strings

            score_list.append({"attempts": attempts, "date": current_time, "name": name, "secret": secret,
                               "wrong guesses": wrong_guesses})

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            break  # break the loop

        elif guess > 10:
            print("Choose number between 1 and 10!")

        elif guess > secret:
            print("Your guess is not correct. Try something smaller.")

        elif guess < secret:
            print("Your guess is not correct. Try something bigger.")

        wrong_guesses.append(guess)


# return all scores
def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


# return top 3
def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list

