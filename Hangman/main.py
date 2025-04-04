import random
def play_hangman():
    words=['banana','apple','cherry','mango','apple','grapes','watermelon','papaya','blueberry','guava']

    word=random.choice(words)
    guessed=[]
    display_words=['_']*len(word)
    attempts=6
    while attempts > 0 :
        print("\nword:",' '.join(display_words))
        print("\nAttempts left: ",attempts)
        guess=input("Enter a letter:")

        if guess in guessed:
            print("you have already guessed this letter")
            continue

        guessed.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i]==guess:
                    display_words[i]=guess
        else:   
            print("wrong guess!!")
            attempts -=1 

        if '_' not in display_words:
            print("You Won!! Congratualtions.")
            print("The word was: ",word)
            return
    print("You lose!! Better luck next time,")
    print("The word was: ",word)

play_hangman()
        


