import random

def play_hangman():
    
    word_list = ["python", "codealpha", "internship", "programmer", "developer"]
    chosen_word = random.choice(word_list)
    guessed_letters = []
    incorrect_attempts_left = 6

    print("====================================")
    print("      Welcome to Hangman Game!      ")
    print("====================================")
    print("Try to guess the secret word.")

    while incorrect_attempts_left > 0:
        displayed_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
                
        print(f"\nWord to guess: {displayed_word.strip()}")
        print(f"Attempts left: {incorrect_attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")     
        
        guess = input("Guess a letter : ").lower().strip()        
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!!! ~ Please enter a single alphabetical letter.")
            continue            
            
        if guess in guessed_letters:
            print(f" You already guessed the letter '{guess}'. Try another one.")
            continue            
            
        guessed_letters.append(guess)        
        
        if guess in chosen_word:
            print(f" Good job!!! '{guess}' is in the word.")
            
            if all(letter in guessed_letters for letter in chosen_word):
                final_word = " ".join([l for l in chosen_word])
                print(f"\nWord to guess: {final_word}")
                print("\n Congratulations! You guessed the word correctly!")
                print(f"The word was: {chosen_word.upper()}")
                break            
        else:
            print(f" Oops!!! '{guess}' is not in the word.")
            incorrect_attempts_left -= 1

    if incorrect_attempts_left == 0:
        print("\n Game Over!!! ~ You ran out of attempts.")
        print(f"The correct word was: {chosen_word.upper()}")
        print("Better luck next time!")

if __name__ == "__main__":
    play_hangman()
