
#class circle 




#create all the different classes for each shape 
#

print("Shape	 Area			    Perimeter:" )
trinagle_formula = print("Triangle  A = ½ × b × h               S = a+b+c")
square_formula = print("Square	  A = a2		      P = 4a")
rectangle_formula = print("rectangle A = l × w		      P = 2(l + w)")






#When comparing all of the different shapes choose area to compare because it is applicable to all of them 






import math

class Circle:
    # Constructor: Initializes the circle with a radius
    def __init__(self, radius, id=1):
        self.radius = radius
        self.id = id

    # Method to calculate area
    def get_area(self):
        return math.pi * (self.radius ** 2)

    # Method to calculate perimeter (circumference)
    def get_perimeter(self):
        return 2 * math.pi * self.radius

    # Method to calculate diameter
    def get_diameter(self):
        return 2 * self.radius

    # Method to display the formatted details
    def display_details(self):
        print(f"\n📊 CIRCLE DETAILS:")
        print(f"│ Shape: Circle #{self.id} │")
        print(f"│ Radius: {self.radius} units │")
        print(f"│ Area: {self.get_area()} units² │")
        print(f"│ Perimeter: {self.get_perimeter()} units │")
        print(f"│ Diameter: {self.get_diameter()} units │")

# --- Main Program Loop ---
print("Enter shape type (1-4): 1")
print("\nCreating a Circle...")

# Get user input for the radius
try:
    r = float(input("Enter radius (positive number): "))
    if r <= 0:
        print("Error: Radius must be a positive number.")
    else:
        # Create an instance of the Circle class
        my_circle = Circle(r, id=1)
        
        print("\n✅ Circle created successfully!")
        
        # Call the method to print the details
        my_circle.display_details()
except ValueError:
    print("Error: Please enter a valid number.")