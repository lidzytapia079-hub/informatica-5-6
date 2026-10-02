def main():
    # not_validated=True
    # while not_validated:
    #     try:
    #         number=int(input("Enter a number between 1 and 10:"))
    #         if number >=1 and number <=10:
    #             print("number stored successfully.")
    #             not_validated = False # -> break
    #         else:
    #             print("That number is not between 1  and 10 .Try again.")




    #     except ValueError:
    #         print("ENTER an interger NUMBER.😒!")
    # while True:
    #     try:
    #         name = input("Enter your name:")
    #         f_letter = name[0]
    #         print("Name stored successsfully.")
    #         break
    #     except IndexError:
    #         print("A name is required.")
    name=""
    while name == "":
        name= input ("Enter your name:")
        if name == "":
            print("A name is required.")
        else:
            print( "Name stored successfully.")




if __name__=="__main__":
    main()
