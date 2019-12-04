# 20 Questions Game
answer = ""
guess = ""
answer = input("Enter your word: ")
counter = 1
while counter <= 20 and guess != answer:
    counter += 1
    guess = input("Enter your guess: ")
    if guess == answer:
        print("Correct! You win")
    if guess != answer:
        print("Oops! Try again")
        
if guess != answer:
    print("Sorry, you're out of guesses")

print("Thanks for playing")