def main():
    p =float(input("how many colombian pesos do you have left?"))
    s=float(input("how many peruvian soles do you have left?"))
    r=float(input("how many brazilian reais do you have left?"))

    mxn = (p* 0.0054) + (s* 5.07)+(r*3.28)
    usd = mxn / 17.06

    print("USD:", round(usd, 2))
    print("MXN:", round(mxn, 2))

if __name__=="__main__":
    main()







