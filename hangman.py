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

def start_game(a):
    with open(a) as  words :
        words = words.read().splitlines()
        word = random.choice(words)
        print(word)
if __name__=="__main__":
    main()

