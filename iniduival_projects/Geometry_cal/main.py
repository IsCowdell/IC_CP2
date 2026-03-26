
#importing all the classes from the file shape
from shapes import Circle, Rectangle, Square, Triangle


# 
#  Utility helpers
# 


def get_positive_float(prompt):
    #Prompt the user for a good number
    #Keeps harrasing until valid input is provided
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("    Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("    Invalid input. Please enter a number.")



    


def print_shape_library(shapes):
    #Display all current shapes inside a box.
    if not shapes:
        lines = [
            "No shapes created yet",
            "Create your first shape below!",
        ]
    else:
        #creeating lines into an empty list 
        lines = []
        #FOR each shape in the shapes list:
        for i, s in enumerate(shapes, 1):
            #add the shape and number and name to lunes add the area to lines and 0petermeter 
            lines.append(f"[{i}] {s.summary_line()}")
            lines.append(f"    Area: {s.area()} units")
            lines.append(f"    Perimeter: {s.perimeter()} units")
    print("SHAPE LIBRARY:")
    print(lines)


# 
#  Menu actions
# 

def create_shape(shapes):
    #Walk the user through creating a new shape and append it to the list.
    print("CREATE NEW SHAPE ")
    print("Available Shapes:")
    print("[1] Circle ")
    print("[2] Rectangle ")
    print("[3] Square ")
    print("[4] Triangle ")

    while True:
        try:
            #givingg the user opuions 
            choice = int(input("Enter shape type (1-4): "))
            #If the number they chouice not in range then raise error 
            if choice not in range(1, 5):
                raise ValueError
            break
        except ValueError:
            print("    Please enter 1, 2, 3, or 4.")
    #asking whatg shape they want to bulidf then taking that shape and pluggin gin the info we need to make it and playing th function for said one
    if choice == 1:
        print("Creating a Circle")
        r = get_positive_float("Enter radius (positive number): ")
        shape = Circle(r)

    elif choice == 2:
        print("Creating a Rectangle")
        l = get_positive_float("Enter length (positive number): ")
        w = get_positive_float("Enter width (positive number): ")
        shape = Rectangle(l, w)

    elif choice == 3:
        print("Creating a Square...")
        s = get_positive_float("Enter side length (positive number): ")
        shape = Square(s)

    else:
        print("Creating a Triangle...")
        print("(Enter the three side lengths and the height)")
        b  = get_positive_float("Enter base: ")
        h  = get_positive_float("Enter height: ")
        a  = get_positive_float("Enter side A: ")
        sb = get_positive_float("Enter side B: ")
        sc = get_positive_float("Enter side C: ")
        shape = Triangle(b, h, a, sb, sc)

    print(f"{shape.name} created successfully")
    shape.display()
    shapes.append(shape)
    input("Press Enter to continue")


def view_all_shapes(shapes):
    #Display details for every shape.
    print("ALL SHAPES ")
    if not shapes:
        print("  No shapes created yet.")
    else:
        for s in shapes:
            s.display()
    input("Press Enter to continue...")


def select_shape(shapes):
    #giving the user the ooptions which shape thehy want 
    print("SELECT SHAPE ")
    if not shapes:
        print("  No shapes to select. Create one first!")
        input("Press Enter to continue...")
        return

    print_shape_library(shapes)
    while True:
        try:
            idx = int(input(f"Enter shape number (1-{len(shapes)}): "))
            if 1 <= idx <= len(shapes):
                break
            raise ValueError
        except ValueError:
            print(f"    Enter a number between 1 and {len(shapes)}.")

    shapes[idx - 1].display_details()
    input("Press Enter to continue...")


def compare_shapes(shapes):
    #Compare area and perimeter of two user-selected shapes.
    print("COMPARE SHAPES ")
    if len(shapes) < 2:
        print("  Need at least 2 shapes to compare")
        input("Press Enter to continue...")
        return

    print_shape_library(shapes)

    def pick(label):
        while True:
            try:
                idx = int(input(f"Select {label} shape number (1-{len(shapes)}): "))
                if 1 <= idx <= len(shapes):
                    return shapes[idx - 1]
                raise ValueError
            except ValueError:
                print(f"Enter a number between 1 and {len(shapes)}.")
##asking the suer for the two shapes they want to compare 
    a = pick("first")
    b = pick("second")
#telling the user the info for each shape and what thhhey need to know 
    print(f"Comparing {a.name} vs {b.name}:")
    print(f"  {'Shape'} {'Area'} {'Perimeter'}")
    print(f"  {a.name} {a.area()} {a.perimeter()}")
    print(f"  {b.name} {b.area()} {b.perimeter()}")

    # Area comparison
    if a.has_larger_area(b):
        print(f"  {a.name} has the larger area.")
    elif b.has_larger_area(a):
        print(f"  {b.name} has the larger area.")
    else:
        print("Both shapes have equal areas.")


def sort_shapes(shapes):
    #Sort and display all shapes by area or perimeter
    print("SORT SHAPES ")
    if not shapes:
        print("  No shapes to sort. Create some first!")
        input("Press Enter to continue")
        return#stop and go to main meno

    print("  Sort by:")
    print("  [1] Area")
    print("  [2] Perimeter")
    #sorting the shapest firn kargest to smallest 
    while True:
        try:
            choice = int(input("Enter choice (1-2): "))
            if choice in (1, 2):
                break
            raise ValueError
        except ValueError:
            print("    Please enter 1 or 2.")

    if choice == 1:
        key_fn = s.area()
    else:
        key_fn = s.perimeter()
    key_name = "Area"                  if choice == 1 else "Perimeter"
    unit     = "units"                 if choice == 1 else "units"

    sorted_shapes = sorted(shapes, key=key_fn, reverse=True)

    print(f"  Shapes ranked by {key_name} (largest  smallest):")
    for rank, s in enumerate(sorted_shapes, 1):
       if choice == 1:
        print(f"  {rank}. {s.summary_line()} {key_name}: {s.area()} {unit}")
    else:
        print(f"  {rank}. {s.summary_line()} {key_name}: {s.perimeter()} {unit}")




def formula1_guide():
    """Show formulas for all shapes."""
    print("FORMULA GUIDE ")
    Circle.formula1_guide()
    Rectangle.formula1_guide()
    Square.formula1_guide()
    Triangle.formula1_guide()
    input("Press Enter to continue")


# 
#  Main loop
# 

def main():
    shapes = []  # holds all created shape objects
#Showing them what they are getting into
    print("GEOMETRY CALCULATOR ")
    print("Welcome to the Shape Calculator!")

    while True:
        print("MAIN MENU ")
        print(f"Current Shapes: {len(shapes)} created")
        print_shape_library(shapes)
#giving them all of their shapes
        print("ACTIONS:")
        print("[1] Create New Shape")
        print("[2] View All Shapes")
        print("[3] Select Shape")
        print("[4] Compare Shapes")
        print("[5] Sort Shapes")
        print("[6] Formula1 Guide")
        print("[7] Quit")
#giving all of the options to choose which one they want
        while True:
            try:
                choice = int(input("Enter your choice (1-7): "))
                if choice in range(1, 8):
                    break
                raise ValueError
            except ValueError:
                print("Please enter a number between 1 and 7.")
#playn=ing the functions assoicated with the option they choose
        if   choice == 1: create_shape(shapes)
        elif choice == 2: view_all_shapes(shapes)
        elif choice == 3: select_shape(shapes)
        elif choice == 4: compare_shapes(shapes)
        elif choice == 5: sort_shapes(shapes)
        elif choice == 6: formula1_guide()
        elif choice == 7:
            print("THANKS FOR NOTHING")
            break


#playing the entire function
main()
