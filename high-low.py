def main():


    def  highest (a, b):


        if a > b :
            print(f"this is the highest number {a}")
            highest_num = a
        else:
            print(f"the highest number is {b}")
            highest_num = b
    num1=int(input("enter your first number:"))
    num2=int(input("enter your second number:"))
    highest(num1,num2)


    def lowest (a, b, c):
        if  a < b and a<c :
            print(f"this is the lowest number {a}")
            lowest_number = a
        elif b<a and b<c :
            print(f"this is the lowest number {b}")
            lowest_number =b
        elif c<a and c<b:

            print(f"this is the lowest number {c}")
            lowest_number = c
        else:
            print("they are equal")

    num3=float(input("enter your first number:"))
    num4=float(input("enter your second number:"))
    num5=float(input("enter your third number:"))
    lowest(num3,num4,num5)





















if __name__=="__main__":
    main()
