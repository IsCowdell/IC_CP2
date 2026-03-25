
# We need math for things like pi and square roots
import math


# This prints a formula cheat sheet when the program starts
print("Shape        Area                       Perimeter:")
print("Triangle     A =   b  h              S = a+b+c")
print("Square       A = a                     P = 4a")
print("Rectangle    A = l  w                  P = 2(l + w)")
print("Circle       A =   r                 P = 2    r")


#  CIRCLE
# 

class Circle:

    # This keeps track of how many circles have been made
    shape_count = 0

    # This runs when you create a new circle
    #making making it give us radius and asking 
    def __init__(self, radius):
        Circle.shape_count += 1       # add 1 to the circle counter
        self.radius = radius          # save the radius
        self.id = Circle.shape_count  # give this circle a number 
        self.name = f"Circle {self.id}"

    # Area = pi times radius squared
    def get_area(self):
        return round(math.pi * self.radius ** 2, 2)

    # Perimeter of a circle is called circumference = 2 times pi times radius
    def get_perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    # Diameter = 2 times the radius (all the way across the circle)
    def get_diameter(self):
        return round(2 * self.radius, 2)

    # These two let the menu on any shape
    def area(self):
        return self.get_area()

    def perimeter(self):
        return self.get_perimeter()

    # This prints all the circle info in a nice box
    def display_details(self):
        lines = [
            f"Shape: {self.name}",
            f"Radius: {self.radius} units",
            f"Area: {self.get_area()} units",
            f"Perimeter: {self.get_perimeter()} units",
            f"Diameter: {self.get_diameter()} units",
        ]
        print("CIRCLE DETAILS:")
        print(lines)

    # The menu uses thisis just displaying all of the details
    def display(self):
        self.display_details()

    # A short one-line description used in the shape list
    def summary_line(self):
        return f"{self.name} (r={self.radius})"

    # This explains the formulas LIKE FORMULA ONEEEEEEEEEEEEEEEEEEEEEEEE
    # not to any specific circle
    @staticmethod
    def formula1_guide():
        print("Circle Formulas:")
        print("  Area      =   r")
        print("  Perimeter = 2    r")
        print("  Diameter  = 2  r")

    # Returns True if this circle has a bigger area than another shape
    def has_larger_area(self, other):
        return self.get_area() > other.get_area()

    # Returns True if this circle has a longer perimeter than another shape
    def has_longer_perimeter(self, other):
        return self.get_perimeter() > other.get_perimeter()
#  RECTANGLE
# 

class Rectangle:

    # Keeps track of how many rectangles have been made
    shape_count = 0

    # This runs when you create a new rectangle
    # Example: my_rect = Rectangle(4, 6)  <-- length 4, width 6
    def __init__(self, length, width):
        Rectangle.shape_count += 1
        self.length = length
        self.width = width
        self.id = Rectangle.shape_count
        self.name = f"Rectangle #{self.id}"

    # Area = length times width
    def get_area(self):
        return round(self.length * self.width, 2)

    # Perimeter = 2 times (length + width)
    def get_perimeter(self):
        return round(2 * (self.length + self.width), 2)

    #finding the diagonal and then just use the tehrom like the pythograms 
    def get_diagonal(self):
        return round(math.sqrt(self.length ** 2 + self.width ** 2), 2)

    # These let the menu call  on any shape
    def area(self):
        return self.get_area()

    def perimeter(self):
        return self.get_perimeter()

    # Prints all the rectangle info in a nice box
    def display_details(self):
        lines = [
            f"Shape: {self.name}",
            f"Length: {self.length} units",
            f"Width: {self.width} units",
            f"Area: {self.get_area()} units",
            f"Perimeter: {self.get_perimeter()} units",
            f"Diagonal: {self.get_diagonal()} units",
        ]
        print("RECTANGLE DETAILS:")
        print(lines)

    def display(self):
        self.display_details()

    def summary_line(self):
        return f"{self.name} ({self.length}{self.width})"

    @staticmethod
    def formula1_guide():
        print("Rectangle Formulas:")
        print("  Area      = l  w")
        print("  Perimeter = 2(l + w)")
        print("  Diagonal  = (l + w)")

    def has_larger_area(self, other):
        return self.get_area() > other.get_area()

    def has_longer_perimeter(self, other):
        return self.get_perimeter() > other.get_perimeter()


# 
#  SQUARE
# 

class Square:

    # Keeps track of how many squares have been made
    shape_count = 0

    # 
    # A square only needs ONE measurement because all sides are equal
    def __init__(self, side):
        Square.shape_count += 1
        self.side = side
        self.id = Square.shape_count
        self.name = f"Square #{self.id}"

    # Area = side times itself (side squared)
    def get_area(self):
        return round(self.side ** 2, 2)

    # Perimeter = 4 times the side (add up all 4 equal sides)
    def get_perimeter(self):
        return round(4 * self.side, 2)

    # Diagonal = the line from one corner to the opposite corner
    def get_diagonal(self):
        return round(self.side * math.sqrt(2), 2)

    # These let the menu call  on any shape
    def area(self):
        return self.get_area()

    def perimeter(self):
        return self.get_perimeter()

    # Prints all the square info in a nice box
    def display_details(self):
        lines = [
            f"Shape: {self.name}",
            f"Side: {self.side} units",
            f"Area: {self.get_area()} units",
            f"Perimeter: {self.get_perimeter()} units",
            f"Diagonal: {self.get_diagonal()} units",
        ]
        print("SQUARE DETAILS:")
        print(lines)

    def display(self):
        self.display_details()

    def summary_line(self):
        return f"{self.name} (s={self.side})"
    #classifes it as a method including it in there 
    @staticmethod
    # DO YOU UNDERSTAND THE REFRENCE Ms larose :)
    def formula1_guide():
        print("Square Formulas:")
        print("  Area      = a")
        print("  Perimeter = 4a")
        print("  Diagonal  = a  2")

    def has_larger_area(self, other):
        return self.get_area() > other.get_area()

    def has_longer_perimeter(self, other):
        return self.get_perimeter() > other.get_perimeter()
#  TRIANGLE
# 

class Triangle:

    # Keeps track of how many triangles have been made
    shape_count = 0

    # This runs when you create a new triangle
    # You need the base, height, and all 3 sides
    def __init__(self, base, height, side_a, side_b, side_c=None):
        Triangle.shape_count += 1
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b

        # If the user gave us side_c, use it to calucatle the A + B = C 
        if side_c is not None:
            self.side_c = side_c
        else:
            self.side_c = round(math.sqrt(side_a ** 2 + side_b ** 2), 4)

        # Give this triangle a number so that it can be added into the 
        self.id = Triangle.shape_count
        self.name = f"Triangle #{self.id}"

    # Area = half of base times height
    def get_area(self):
        return round(0.5 * self.base * self.height, 2)

    # Perimeter = add up all three sides
    def get_perimeter(self):
        return round(self.side_a + self.side_b + self.side_c, 2)

    # These let the menu call area() and perimeter() on any shape
    def area(self):
        return self.get_area()

    def perimeter(self):
        return self.get_perimeter()

    # Prints all the triangle info in a veryyy nice box
    def display_details(self):
        lines = [
            f"Shape: {self.name}",
            f"Base: {self.base} units",
            f"Height: {self.height} units",
            f"Sides: {self.side_a}, {self.side_b}, {self.side_c}",
            f"Area: {self.get_area()} units",
            f"Perimeter: {self.get_perimeter()} units",
        ]
        print("TRIANGLE DETAILS:")
        print(lines)

    def display(self):
        self.display_details()

    def summary_line(self):
        return f"{self.name} (b={self.base}, h={self.height})"

    @staticmethod
    def formula1_guide():
        print("Triangle Formulas:")
        print("  Area      =   b  h")
        print("  Perimeter = a + b + c")

    def has_larger_area(self, other):
        return self.get_area() > other.get_area()

    def has_longer_perimeter(self, other):
        return self.get_perimeter() > other.get_perimeter()
