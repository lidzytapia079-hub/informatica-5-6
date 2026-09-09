import random
def main():
    name=input("Hello! What is your name? :" )
    #f por q hay vavriables y texto en el mismo print
    print(f"Well,{name} I am thinking of a number between 1 and 100.")
    #start with a random number
    guess = 0
    number = random.randint(1,100)

    while guess !=number:

        guess = int(input("take a guess:"))
        if guess > number:
            print("Your guess is too high")

        elif guess < number:
            print("Your guess is to low!")

        else:
            print(f"Good job,{name}! You guessed my number! ")
            break




if __name__=="__main__":
    main()

