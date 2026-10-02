def main():
    print("Welcome to the times table quiz.")
    not_validated= True
    while not_validated:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))
            while not_validated:
                try:

                    max_value=int(input("Enter the maximum value for your times table: "))

                    if 1 <= times_table <= 10:
                        while True:
                            try:
                                print(f"Here is your quiz on  {times_table} times table")

                                for x in range(1,max_value+1):
                                    answer = x * times_table
                                    useranswer = int(input(f"{x} times table{times_table}is?"))
                                    if useranswer==answer:
                                        print("correct")

                            except ValueError:
                                    print("you have to enter a number")





                    else:
                        print("incorrect.")




if __name__ == "__main__":
    main()


