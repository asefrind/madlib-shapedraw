# Shape Drawing

def TriangleDraw():
    print("     /|")
    print("    / |")
    print("   /  |")
    print("  /___|")

def SquareDraw():
    print("----------------")
    print("|               |")
    print("|               |")
    print("|               |")
    print("|               |")
    print("----------------")

def RandomDraw():
    print("|  - -  -  -   -   - | | |      |")
    print(" | -   -   -   -   -  |       |")
    print("  |  -   -   -   -  |  |     |")
    print("   |   -   |    -  -   |    |")
    print("    ||  |       -    -    |")
    print("     |___________________|")

# Let user choose which shape to draw

i = 1
while i < 4:
    selector = input("Choose between: Square/Triangle/Random: ")
    if selector == "Square":
        print(SquareDraw())
    
    elif selector == "Triangle":
        print(TriangleDraw())
    
    elif selector == "Random":
        print(RandomDraw())

    i = i + 1