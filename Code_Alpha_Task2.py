import random

def hangman():
    # Predefined list of words
    words = ["python", "java", "hangman", "coding", "program"]
    word = random.choice(words)  # randomly choose a word
    
    guessed_letters = []  # store guessed letters
    attempts = 6  # number of wrong attempts allowed
    
    print("Welcome to Hangman!")
    print("_ " * len(word))  # display blanks for the word
    
    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
        
        # Display the word with guessed letters revealed
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(display_word.strip())
        
        # Check if player has guessed the whole word
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word!")
            break
    else:
        print(f"\n😢 You ran out of attempts! The word was '{word}'.")

# Run the game
hangman()