#create a txt file with all the words.
#Define the main fuction
#use with to open the txt file
#define an other function
#use inputs to print
#call the function to start the game
#make a list of letters
#use ln fuction to count the words
#a counter to count le lives , count of mistakes
#uae a while loop to ask to the user many times
#use random function to adivinar the  word
#use file.read to read the contengt in the text
#the program will give the  welcome to the user
#create a variable to save there the list of our txt list of words
#then with print we ask to the user than  insert they first guest according with or functon while
#put if , because if the user print a letter good one print "you have almost the idea"
#use an elif for put the condition if the people dont pass of the number of chances print"still playing"
#then if th user dont put a letter use the function else to put invalid answer
#if the user win put a print than will said "congragulation you won"
#if the userr fail with try and exept , put , try again
import random

def main():
    start_game("words.txt")
def start_game(file):

    with open(file) as f:
        word_bank = f.read().splitlines()
    word = random.choice(word_bank)
    attempts = 10
    hint = ["_"] * len(word)
    incorrect_letters=[]
    while attempts > 0:
        print("Current word:", " ".join(hint))
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1:
                break
            else:
                print("Invalid guess. Try again.")
            if guess in word and guess not in hint:
                for i in range(len(word)):
                    if word[i] == guess:
                        hint[i] = guess
                print("Great guess!")
            elif guess in hint:

                print("You already guessed that letter! Attempts left:", str(attempts))
            else:
                attempts -= 1
                print("Wrong guess! Attempts left:", str(attempts))

                if guess not in incorrect_letters:
                    incorrect_letters.append(guess)
                print(f"Incorrect letters: {" ".join(incorrect_letters)}")

            if "_" not in hint:
                print("Congratulations! 🥳 You guessed the word:", word)
                break
            if attempts == 0 and "_" in hint:
                print("No attempts left 💀 The word was:", word)
if __name__=="__main__":
    main()

