#Author: Laltu Sardar


import string
import random

# Global Constants
WORDLE_SIZE = 5
GUESS_NUM = 0
GUESS_MAX = 6
alphabets = string.ascii_uppercase
WORDLE = [['-'] * WORDLE_SIZE for i in range(GUESS_MAX)]
TARGET_WORD = "BLANK"
WORD_LIST = []

# Class to define text colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Function to display the keyboard (not implemented)
def keyboard_display(): 
    return

# Function to display the wordle
def wordle_display():
    global WORDLE
    global WORDLE_SIZE
    global alphabets
    
    # Dictionary to track the appearance of letters
    alpha_dict = dict.fromkeys(alphabets, 0)
    # 0 -- not appeared, 1 bold, 2 yellow, 3 green
    
    # Iterate over each row in the wordle
    for row in WORDLE:
        modified_row = row.copy()
        # Check each character in the row
        for i in range(WORDLE_SIZE):
            if row[i] == TARGET_WORD[i]:
                # If character is in the right position in the target word, display in green
                modified_row[i] = color.GREEN + color.BOLD + modified_row[i] + color.END 
                alpha_dict[row[i]] = 3
            elif row[i] in TARGET_WORD:
                # If character is in the target word but not in the right position, display in yellow
                modified_row[i] = color.YELLOW + color.BOLD + modified_row[i] + color.END
                if alpha_dict.get(row[i]) < 2:
                    alpha_dict[row[i]] = 2
            elif row[i] in alphabets:
                # If character is not in the target word, display normally
                modified_row[i] = color.BOLD + modified_row[i] + color.END   
                if alpha_dict.get(row[i]) < 1:
                    alpha_dict[row[i]] = 1
        # Print the modified row
        tmp_str = modified_row[0]
        for i in range(WORDLE_SIZE-1):
            tmp_str = tmp_str + "  " + modified_row[i+1]
        print(tmp_str)
    
    # Generate string to display the appearance of each letter
    alph_str = []
    for letter in alphabets:
        if alpha_dict[letter] == 3:
            alph_str += color.GREEN + color.BOLD + letter + color.END + " "
        elif alpha_dict[letter] == 2:
            alph_str += color.YELLOW + color.BOLD + letter + color.END + " "
        elif alpha_dict[letter] == 1:
            alph_str += letter + " "
        else:
            alph_str += color.RED + color.BOLD + letter + color.END + " "
            
    print("-----------------------------------------------------")             
    print(''.join(alph_str))
    print("-----------------------------------------------------")
       
    return
        
# Function to initialize the wordle
def wordle_init():
    global TARGET_WORD
    TARGET_WORD= random.choice(WORD_LIST)
    return
    
# Function to initialize the list of words from a text file
def list_of_words_init():
    global WORD_LIST
    global alphabets
    # Open the text file containing English words
    f = open("words_alpha.txt", "r")
    for word in f.readlines():
        # Select only words of the desired length
        if len(word) == 6:
            word = word.replace("\n", "") 
            word = word.upper()
            flag = 0
            # Check if all characters in the word are alphabets
            for i in range(5):
                if word[i] not in alphabets:
                    flag = 1
                    break
            if flag == 0:        
                WORD_LIST.append(word)
    f.close()
    return

# Function to validate user input
def validate_input(guess_word):
    global WORDLE_SIZE
    global WORD_LIST
    guess_word = guess_word.upper()
    if len(guess_word) != WORDLE_SIZE:
        print("Wrong word size. The guessed word should be of length", WORDLE_SIZE)
        return 0
    if guess_word not in WORD_LIST:
        print("Guessed word is not in the English dictionary. Try another.")
        return 0           
    else:
        return 1
       
# Function to play the game
def play_game():
    global WORDLE
    global GUESS_MAX
    global WORDLE_SIZE
    global TARGET_WORD
    for guess in range(GUESS_MAX):
        inp_validity = 0
        while inp_validity == 0:
            guess_word = input("Give your guess: ")
            guess_word = guess_word.upper()
            inp_validity = validate_input(guess_word)
        for i in range(WORDLE_SIZE):
            WORDLE[guess][i] = guess_word[i]
        wordle_display()
        keyboard_display()
        if guess_word == TARGET_WORD:
            return 1
    return 0

# Function to display welcome message and game instructions
def show_welcome_msg():
     # 0 -- not appeared, 1 bold, 2 yellow, 3 green
    print("====================================================")
    print("\nThis is a wordle game of 5 words")
    print("----------------------------------")
    print("Maximum 6 guesses are allowed")
    print("Green indicates: Letter is present in the word but it is in the right place.")
    print("Blue indicates: Letter is present in the word but not in right place.")
    print("White indicates: Letter is present but not in right place.")
    print("Orange indicates: Letter is not searched yet")
    print("=====================================================/n")
    
# Main function
def main():
    global TARGET_WORD
    show_welcome_msg()    
    list_of_words_init()
    wordle_init()
    wordle_display()
    
    output = play_game()
    if output == 1:
        print("WOW! You have WON!!!")
    else:
        print("You have LOST the game. Better luck next time.")
    
    print("The HIDDEN word was:", TARGET_WORD)

# Check if this module is being run as the main program
if __name__ == "__main__":
    main()

