def main ():
    #Augmented assigment operator
    money= 5
    money +=10
    print(money)# This will print 15

    #Substraction assigment operator
    minutes = 60
    minutes = minutes-25
    print (minutes) #This will print 35

    # Multiplication assigment operator
    num= 10
    num *= 4
    print (num)
    skill= 10
    skill *= 2
    print (skill)

    #Division assigment operator
    pizzas= 8
    people = int(input("number of proplr at the pizza party:"))
    pizzas/=4
    print (pizzas)

    #Modulus Assigment operator
    num1=10
    num2=5
    num1%=num2
    print(num1)
    leftover= 8
    leftover%=people
    print(leftover)

if __name__== "__main__":
    main()
