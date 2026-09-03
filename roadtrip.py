def main():
    answer = "" #1Initialize
    followup=""

    while answer !="Yes!": #2Condition
        answer=input("Are we there yet?").strip().title() #3Update
        if answer=="Yes":
            followup=input("Really?").strip().title()
        if followup=="Yes!":
            break

    print("we just arrived!")



if __name__=="__main__":
    main()
