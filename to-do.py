def main():
    tasks=[]
    new_task=""
    ask=""
    while True:
        print(f"You have{len(tasks)}tasks to do .")
        print(tasks)
        command=input("What do you want to do ?(add, complete, or end):").lower()
        if command=="add":
            new_task=input("enter a new task:")
            tasks.append(new_task)
        elif command =="end":
            break
        elif command == "complete":
            ask = input("Have you finished all of them?").strip().lower()
            if ask  == "yes":
                tasks.clear()
                print("you finished all of them")
                break
            else:
                tasks.remove(input("what  did you finish?"))
                print(tasks)
                if tasks==[]:
                    print("you finished")
                    break
                elif answer=="exit ":
                    break

if __name__ == "__main__":
    main()

