import random  # Importing the random module to choose a random word

def play_hangman():
    # List of possible words for the game
    words = ['banana', 'apple', 'cherry', 'mango', 'apple', 'grapes', 'watermelon', 'papaya', 'blueberry', 'guava']

    # Select a random word from the list
    word = random.choice(words)
    
    guessed = []  # List to keep track of guessed letters
    display_words = ['_'] * len(word)  # Display underscores for unguessed letters
    attempts = 6  # Number of attempts allowed

    while attempts > 0:  # Loop until the player runs out of attempts
        # Display the current progress of the word
        print("\nWord:", ' '.join(display_words))
        print("\nAttempts left:", attempts)
        
        # Ask the player for a letter guess
        guess = input("Enter a letter: ").lower()

        # Check if the letter was already guessed
        if guess in guessed:
            print("You have already guessed this letter.")
            continue  # Skip the rest of the loop and ask for another letter

        guessed.append(guess)  # Add the guessed letter to the list

        # Check if the guessed letter is in the word
        if guess in word:
            # Replace underscores with the correctly guessed letter
            for i in range(len(word)):
                if word[i] == guess:
                    display_words[i] = guess
        else:
            print("Wrong guess!!")
            attempts -= 1  # Reduce the number of attempts for an incorrect guess

        # Check if the word has been fully guessed
        if '_' not in display_words:
            print("You Won!! Congratulations.")
            print("The word was:", word)
            return  # End the function since the player has won

    # If the player runs out of attempts, they lose the game
    print("You lose!! Better luck next time.")
    print("The word was:", word)

# Start the Hangman game
play_hangman()

