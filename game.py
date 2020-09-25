some_num = 32 #hard-code

guess = int(input("Please guess the secret number: "))

if guess == some_num:
    print("Congratulations!")
else:
    print("Sorry, try one more time.")