import random
def main():
    name=input("Hello! What is your name? :" )
    print(f"Well,{name} I am thinking of a number between 1 and 100.")
    guess = ""
    number=random.radint(1,100)

    while guess !=number:

    guess=int(input("take a guess:"))
    if guess > number:
        print("Your guess is too high")
    elif gues < number:
        print("Your guess is to low!")
        break

    print(f"Good job,{name}! You guessed my number! ")




if __name__=="__main__":
    main()

