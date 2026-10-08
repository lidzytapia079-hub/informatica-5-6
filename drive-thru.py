def main():
    welcome()
    choice=int(input("select  your order:"))
    get_item(choice)




def welcome ():
    menu=["Cheeseburger","Fries","Soda","Ice Cream","Cookie"]
    print("welcome to the restaurant !")
    print("Here's tghe menu:")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")






def  get_item(order):
    if order == 1:
        print("🍔")

    elif order == 2:
        print("🍟")
    elif order == 3:
        print("🥤")
    elif order == 4:
         print("🍦")
    elif order == 5:
        print("🍪")

    else:
        print("invalid option")











if __name__=="__main__":
    main()
