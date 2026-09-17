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
        elif answer == complete:
            ask = input()




if __name__ == "__main__":
    main()

