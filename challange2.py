import random
def main():
    att= 6

    name=input("Hello! What is your name? :" )
    print(f"Well,{name} I am thinking of a number between 1 and 100.")
    guess = ""
    number = random.randint(1,100)

    while guess !=number:
        att-=1

        guess = int(input("take a guess:"))
        if att== 0:
            print("game over")
            break
        if guess > number:
            print(f"Your guess is too high. Attempts: {att}")

        elif guess < number:
            print(f"Your guess is too low. Attempts: {att}")
        else:
            print(f"Good job,{name}! You guessed my number! ")
            break




if __name__=="__main__":
    main()
