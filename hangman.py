#importing the random and time modules
#Import random: This is used to randomly choose an item from a list [] or basically a sequence.
#Import time: This module is used to import the actual time from your pc to use in the program.
import random
import time

# Initial Steps to invite in the game:
print("\nWelcome to Hangman game by DataFlair\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

'''We define the main function that initializes the arguments:
 global count, global display, global word, global already_guessed, 
 global length and global play_game. They can be used further in other functions
  too depending on how we want to call them'''
def main():
    global count
    global word
    global already_guessed
    global length
    global play_game
    #Words_to_guess: Contains all the Hangman words we want the user to guess in the game.
    words_to_guess =["january", "border", "image", "film", "promise", "kids","lungs","doll","rhyme","damage","plants"]
    #Word: we use the random module in this variable to randomly choose the word from words_to_guess in the game.
    word = random.choice(words_to_guess)
    #Length: len() helps us to get the length of the string.
    length = len(word)
    #Count: is initialized to zero and would increment in the further code.
    count = 0
    #Display: This draws a line for us according to the length of the word to guess.
    display = '_' * length
    #Already_guessed: This would contain the string indices of the correctly guessed words.
    already_guessed = []
    play_game = ""
    
    #a loop to re-execute the game when the first round eds:
    #Play_loop: This function takes in the argument of play_game.
    def play_loop():
        global play_game
        #Play_game: We use this argument to either continue the game after it is played once or end it according to what the user suggests
        play_game = input(" Do You Want To Playagain? y = yes, n = no \n")
        
        """Play_game: We use this argument to either continue the game after it 
        is played once or end it according to what the user suggests"""
        #While loop is used to execute the play_game argument.
        while paly_game not in ["y", "n", "Y", "N"]:
            play_game = input("Do you want to play again? y = yes, n = no \n")
        if play_game =="y":
            main()
        elif play_game =="n":
            print("Thank for playing ! We Axpect You Back Again")
            exit()

# Initializing all the conditions required fro the game:
"""We call all the arguments again under the hangman() function.
Limit: It is the maximum guesses we provide to the user to guess a particular word.
Guess: Takes the input from the user for the guessed letter. Guess.strip() removes the letter from the given word.
If loop checks that if no input is given, or two letters are given at once, or a number is entered as an input, 
it tells the user about the invalid input and executes hangman again."""
# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index +1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * lenght:
        print("Congrats....! you have guessed correct word")
        play_loop()

    elif count != limit:
        hangman()
main()

             

        



  



