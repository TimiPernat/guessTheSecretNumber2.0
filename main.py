import datetime
import json
import random

secret = random.randint(1, 30)
date = datetime.datetime.now()


def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def get_top_scores():
    score_list = get_score_list()
    top_scores = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_scores


def play_game(difficulty):
    score_list = get_score_list()
    attempts = 0

    if difficulty == "easy":
        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1

            if guess == secret:
                score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
                with open("score_list.json", "w") as score_file:
                    score_file.write(json.dumps(score_list))
                    print("You've guessed it - congratulations! It's number " + str(secret))
                    print("Attempts needed: " + str(attempts))
                break
            elif guess > secret:
                print("Your guess is not correct... try something smaller")
            elif guess < secret:
                print("Your guess is not correct... try something bigger")
    elif difficulty == "hard":
        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1

            if guess == secret:
                score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
                with open("score_list.json", "w") as score_file:
                    score_file.write(json.dumps(score_list))
                    print("You've guessed it - congratulations! It's number " + str(secret))
                    print("Attempts needed: " + str(attempts))
                break


print(get_top_scores())

while True:
    user_difficulty = input("On what difficulty do you want to play (easy/hard): ")
    play_game(user_difficulty)
    repeat = input("Do you want to exit or play again: ")
    if repeat == "play":
        attempts = 0
        secret = random.randint(1, 30)
    elif repeat == "exit":
        break
