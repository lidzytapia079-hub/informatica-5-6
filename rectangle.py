def main():
    width  = int(input(("Enter the width of the rectangle: ")))
    print("o"*width)
    print("o"*width)
    print("o"*width)
    print("o"*width)
    print("o"*width)
    p= (5 * 2)+(width * 2)
    print("perimetrer:",p)
    AREA=width *5
    print(f"This is the rectangle: {AREA}")
    Diagonal=(width**2+5**2)**0.5
    print(f"This is the rectanle´s diagonal:{Diagonal}")
    perimeter=(width+5)*2
    print(f"This is the perimeter;{perimeter}")


if __name__ == "__main__":
    main()
