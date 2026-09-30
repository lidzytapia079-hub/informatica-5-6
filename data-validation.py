def main():
    not_validated=True
    while not_validated:#while true#intena algo a exept errors
        try:
            number=int(input("Enter a number between 1 and 10:"))
            print("number stored successfully.")
            if 1<=number<=10:
                print("number stored successfully." )

            else:
                print("Enter a number between 1 and 10:")
                continue


            not_validated = False # -> break

        except ValueError:
            print("ENTER an interger NUMBER.😒!")




if __name__=="__main__":
    main()
