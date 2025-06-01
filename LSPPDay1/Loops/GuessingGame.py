secret_word= "pizza"
guess= ""  # all guesses stored here
guess_count = 0   # how many guessese have been made
guess_limit= 3 # Maximum number of guesses allowed
out_of_guesses= False  # whether the user has run out of guesses

# Loop until the user guesses the secret word
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess= input("Guess the secret word: ")
        guess_count += 1  # Increment the guess count
    else:
        out_of_guesses = True

# Check if the user has run out of guesses
if out_of_guesses:
    print("Sorry, you've run out of guesses.")
else: 
    print("Congratulations! You've guessed the secret word.")
   


 
        