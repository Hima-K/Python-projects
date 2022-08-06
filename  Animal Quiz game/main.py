def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ", answer)


score = 0
print("Guess the Animal")
guess1 = input("Which bird is considered to be the largest bird in the world?")
check_guess(guess1, "ostrich")
guess2 = input(" Which animal, also considered the largest land mammal in the world, cannot jump?")
check_guess(guess2, "elephant")
guess3 = input(" Which animal has the most extended tail? ")
check_guess(guess3, "giraffe")
print("Your Score is " + str(score))