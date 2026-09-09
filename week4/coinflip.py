import random
def main():
    #question
    guess = int(input("heads or tails (1 for heads, 2 for tails) "))

    #randomizer
    coin = random.randint(1,2)
    if coin == 1:
        print("heads")
    elif coin == 2:
        print("tails")

    #formula for question
    if coin == guess:
        print("You Won!")
    elif coin != guess:
        print("you lost")


if __name__=="__main__":
    main()






