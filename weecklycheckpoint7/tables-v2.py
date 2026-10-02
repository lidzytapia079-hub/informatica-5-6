def main():
    print("Welcome to the times table quiz")
    not_validated = True
    while not_validated:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))
            if 1 <= times_table <= 10:
                not_validated = False
        except ValueError:
            print("Enter a whole number!")

    not_validated2 = True
    while not_validated2:
    try:
        max_value = int(input("Enter the maximum value for your times table: "))
        not_validated2 = False
    except ValueError:
        print("Enter a whole number!")


        print(f"Here is your quiz on the {times_table} times table")

        for x in range(1, max_value+1):
            answer = x * times_table
            print(f"{x} times {times_table} is...")
            not_validated3 = True


            while not_validate3:
                try:

            user_answer = int(input("answer: "))
            if user_answer == answer:
                print("correct!")
                except ValueError:
        print("Enter a whole number!")

            else:
                print("incorrect!")
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
