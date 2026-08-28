def main():
    print("ratatuill's carbon grill")
    rating =float(input("What is your opinion about ratatuill's carbon grill in a of  scale 0-5?:" ))
    if rating > 4.5:
        print("perfection")
    elif rating > 4:
        print("exelent")
    elif rating > 3:
        print("good")
    elif rating > 2:
        print("fair")

    else:
        print("poor")

if __name__=="__main__":
    main()
